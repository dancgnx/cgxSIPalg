#!/usr/bin/env python3
import cgxinit
from cloudgenix import jd, jd_detailed
import sys
import logging


def listALG(cgx,args,sites):
    """
    list the alg objects for all IONs
    """
    for element in cgx.get.elements().cgx_content["items"]:

        # check if element is a spoke
        if element["site_id"] in sites:
            log.info("Listin ALG for {element} at {site}".format( element=element["name"], site=sites[element["site_id"]]))
            for extension in cgx.get.element_extensions(element["site_id"], element["id"]).cgx_content["items"]:
                if extension["namespace"] == "algconfig":
                    jd(extension)
def updateSIPalg(cgx,args,sites):
    """
    change SIP alg accoring to the args input
    """
    # for every elemnt, check if it should be changed and if it should do the required change
    for element in cgx.get.elements().cgx_content["items"]:

        # if element ID isn't in the sites list, its a hub and we can ignore it
        if not element["site_id"] in sites:
            continue

        # check if the element should be changed
        if args["scope_all"]:
            # first check if extension exist
            log.info("{element} at {site} is being configured".format(
                element=element["name"], site=sites[element["site_id"]]))
            alg = None
            for extension in cgx.get.element_extensions(element["site_id"], element["id"]).cgx_content["items"]:
                if extension["namespace"] == "algconfig":
                    alg = extension
                    log.info("-- already have algconfig")
                    break

            # if alg do not exists create on
            if not alg:
                log.info("-- creating algconfig name space")
                ext = {
                    "name": "alg",
                    "namespace": "algconfig",
                    "entity_id": None,
                    "disabled": False,
                    "conf": {
                        "rules": []
                    }
                }
                r = cgx.post.element_extensions(
                    element["site_id"], element["id"], ext)
                if not r:
                    jd_detailed(r)
                    raise ValueError("cant create algconfig extenstion")
                alg = r.cgx_content
            
            # if rules is None then create a list
            if not alg["conf"]["rules"]:
                alg["conf"]["rules"] = []

            # find SIP alg rule
            rule_found = False
            for i in range(len(alg["conf"]["rules"])):
                #if found set the enable
                if alg["conf"]["rules"][i]["alg"] == "SIP":
                    log.info("-- SIP alg found. Updating")
                    rule_found = True
                    alg["conf"]["rules"][i]["enabled"] = args["enable_alg"]
                    break

            # if SIP alg not found append it to the rules
            if not rule_found:
                log.info("-- SIP alg not found. adding sip rule")
                alg["conf"]["rules"].append(
                    {
                        "alg":"SIP",
                        "enabled": args["enable_alg"]
                    }
                )
            
            # update the rules
            log.info("-- updating alg entry")
            r = cgx.put.element_extensions(element["site_id"], element["id"], alg["id"],alg)
            if not r:
                jd_detailed(r)
                raise ValueError("cant update alg extension")


if __name__ == "__main__":
    # init cloudgenix object and get command line arguments
    cgx, args = cgxinit.go()

    #init logging
    logging.basicConfig(level=logging.INFO)
    log=logging.getLogger("cgxSIPalg")

    #build site dist
    sites={}
    for site in cgx.get.sites().cgx_content["items"]:
        # we only care about spoke sites as hub sites don't do NAT
        if site["element_cluster_role"] == "SPOKE":
            sites[site["id"]] = site["name"]
    if args["list"]:
        listALG(cgx,args,sites)
    else:
        updateSIPalg(cgx,args,sites)        
