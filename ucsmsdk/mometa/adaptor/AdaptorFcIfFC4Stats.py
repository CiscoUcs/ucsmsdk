"""This module contains the general information for AdaptorFcIfFC4Stats ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class AdaptorFcIfFC4StatsConsts:
    CONTROL_REQUESTS_NA = "NA"
    CONTROL_REQUESTS_DELTA_NA = "NA"
    CONTROL_REQUESTS_DELTA_AVG_NA = "NA"
    CONTROL_REQUESTS_DELTA_MAX_NA = "NA"
    CONTROL_REQUESTS_DELTA_MIN_NA = "NA"
    INPUT_MEGABYTES_NA = "NA"
    INPUT_MEGABYTES_DELTA_NA = "NA"
    INPUT_MEGABYTES_DELTA_AVG_NA = "NA"
    INPUT_MEGABYTES_DELTA_MAX_NA = "NA"
    INPUT_MEGABYTES_DELTA_MIN_NA = "NA"
    INPUT_REQUESTS_NA = "NA"
    INPUT_REQUESTS_DELTA_NA = "NA"
    INPUT_REQUESTS_DELTA_AVG_NA = "NA"
    INPUT_REQUESTS_DELTA_MAX_NA = "NA"
    INPUT_REQUESTS_DELTA_MIN_NA = "NA"
    OUTPUT_MEGABYTES_NA = "NA"
    OUTPUT_MEGABYTES_DELTA_NA = "NA"
    OUTPUT_MEGABYTES_DELTA_AVG_NA = "NA"
    OUTPUT_MEGABYTES_DELTA_MAX_NA = "NA"
    OUTPUT_MEGABYTES_DELTA_MIN_NA = "NA"
    OUTPUT_REQUESTS_NA = "NA"
    OUTPUT_REQUESTS_DELTA_NA = "NA"
    OUTPUT_REQUESTS_DELTA_AVG_NA = "NA"
    OUTPUT_REQUESTS_DELTA_MAX_NA = "NA"
    OUTPUT_REQUESTS_DELTA_MIN_NA = "NA"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorFcIfFC4Stats(ManagedObject):
    """This is AdaptorFcIfFC4Stats class."""

    consts = AdaptorFcIfFC4StatsConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcIfFC4Stats", "adaptorFcIfFC4Stats", "fc-if-fc4-stats", VersionMeta.Version111j, "OutputOnly", 0xf, [], ["admin", "operations", "read-only"], ['adaptorHostFcIf'], ['adaptorFcIfFC4StatsHist'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111j, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "control_requests": MoPropertyMeta("control_requests", "controlRequests", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "control_requests_delta": MoPropertyMeta("control_requests_delta", "controlRequestsDelta", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "control_requests_delta_avg": MoPropertyMeta("control_requests_delta_avg", "controlRequestsDeltaAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "control_requests_delta_max": MoPropertyMeta("control_requests_delta_max", "controlRequestsDeltaMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "control_requests_delta_min": MoPropertyMeta("control_requests_delta_min", "controlRequestsDeltaMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []),
        "input_megabytes": MoPropertyMeta("input_megabytes", "inputMegabytes", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_megabytes_delta": MoPropertyMeta("input_megabytes_delta", "inputMegabytesDelta", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_megabytes_delta_avg": MoPropertyMeta("input_megabytes_delta_avg", "inputMegabytesDeltaAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_megabytes_delta_max": MoPropertyMeta("input_megabytes_delta_max", "inputMegabytesDeltaMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_megabytes_delta_min": MoPropertyMeta("input_megabytes_delta_min", "inputMegabytesDeltaMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_requests": MoPropertyMeta("input_requests", "inputRequests", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_requests_delta": MoPropertyMeta("input_requests_delta", "inputRequestsDelta", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_requests_delta_avg": MoPropertyMeta("input_requests_delta_avg", "inputRequestsDeltaAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_requests_delta_max": MoPropertyMeta("input_requests_delta_max", "inputRequestsDeltaMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "input_requests_delta_min": MoPropertyMeta("input_requests_delta_min", "inputRequestsDeltaMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "intervals": MoPropertyMeta("intervals", "intervals", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "output_megabytes": MoPropertyMeta("output_megabytes", "outputMegabytes", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_megabytes_delta": MoPropertyMeta("output_megabytes_delta", "outputMegabytesDelta", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_megabytes_delta_avg": MoPropertyMeta("output_megabytes_delta_avg", "outputMegabytesDeltaAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_megabytes_delta_max": MoPropertyMeta("output_megabytes_delta_max", "outputMegabytesDeltaMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_megabytes_delta_min": MoPropertyMeta("output_megabytes_delta_min", "outputMegabytesDeltaMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_requests": MoPropertyMeta("output_requests", "outputRequests", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_requests_delta": MoPropertyMeta("output_requests_delta", "outputRequestsDelta", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_requests_delta_avg": MoPropertyMeta("output_requests_delta_avg", "outputRequestsDeltaAvg", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_requests_delta_max": MoPropertyMeta("output_requests_delta_max", "outputRequestsDeltaMax", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "output_requests_delta_min": MoPropertyMeta("output_requests_delta_min", "outputRequestsDeltaMin", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["NA"], ["0-18446744073709551615"]),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []),
        "update": MoPropertyMeta("update", "update", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "controlRequests": "control_requests", 
        "controlRequestsDelta": "control_requests_delta", 
        "controlRequestsDeltaAvg": "control_requests_delta_avg", 
        "controlRequestsDeltaMax": "control_requests_delta_max", 
        "controlRequestsDeltaMin": "control_requests_delta_min", 
        "dn": "dn", 
        "inputMegabytes": "input_megabytes", 
        "inputMegabytesDelta": "input_megabytes_delta", 
        "inputMegabytesDeltaAvg": "input_megabytes_delta_avg", 
        "inputMegabytesDeltaMax": "input_megabytes_delta_max", 
        "inputMegabytesDeltaMin": "input_megabytes_delta_min", 
        "inputRequests": "input_requests", 
        "inputRequestsDelta": "input_requests_delta", 
        "inputRequestsDeltaAvg": "input_requests_delta_avg", 
        "inputRequestsDeltaMax": "input_requests_delta_max", 
        "inputRequestsDeltaMin": "input_requests_delta_min", 
        "intervals": "intervals", 
        "outputMegabytes": "output_megabytes", 
        "outputMegabytesDelta": "output_megabytes_delta", 
        "outputMegabytesDeltaAvg": "output_megabytes_delta_avg", 
        "outputMegabytesDeltaMax": "output_megabytes_delta_max", 
        "outputMegabytesDeltaMin": "output_megabytes_delta_min", 
        "outputRequests": "output_requests", 
        "outputRequestsDelta": "output_requests_delta", 
        "outputRequestsDeltaAvg": "output_requests_delta_avg", 
        "outputRequestsDeltaMax": "output_requests_delta_max", 
        "outputRequestsDeltaMin": "output_requests_delta_min", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "update": "update", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.control_requests = None
        self.control_requests_delta = None
        self.control_requests_delta_avg = None
        self.control_requests_delta_max = None
        self.control_requests_delta_min = None
        self.input_megabytes = None
        self.input_megabytes_delta = None
        self.input_megabytes_delta_avg = None
        self.input_megabytes_delta_max = None
        self.input_megabytes_delta_min = None
        self.input_requests = None
        self.input_requests_delta = None
        self.input_requests_delta_avg = None
        self.input_requests_delta_max = None
        self.input_requests_delta_min = None
        self.intervals = None
        self.output_megabytes = None
        self.output_megabytes_delta = None
        self.output_megabytes_delta_avg = None
        self.output_megabytes_delta_max = None
        self.output_megabytes_delta_min = None
        self.output_requests = None
        self.output_requests_delta = None
        self.output_requests_delta_avg = None
        self.output_requests_delta_max = None
        self.output_requests_delta_min = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.update = None

        ManagedObject.__init__(self, "AdaptorFcIfFC4Stats", parent_mo_or_dn, **kwargs)
