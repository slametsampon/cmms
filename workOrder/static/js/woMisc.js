/*Function for get status work order base on code*/
function getStatus(stsCode){
    var status = ""
    switch (stsCode) {
        case "op":
            status = "Open";
            break;
        case "cl":
            status = "Close";
            break;
        case "ck":
            status = "Check";
            break;
        case "rv":
            status = "Revise";
            break;
        case "ap":
            status = "Approve";
            break;
        case "rw":
            status = "Review";
            break;
        case "rj":
            status = "Reject";
            break;
        case "sc":
            status = "Scedule";
            break;
        case "rt":
            status = "Return";
            break;
        case "ns":
            status = "Need Shutdown";
            break;
        case "nl":
            status = "Need Materials";
            break;
        case "nm":
            status = "Need MOC";
            break;
        case "ec":
            status = "Execute";
            break;
        case "cm":
            status = "Complete";
            break;
        case "fn":
            status = "Finish";
            break;
        case "cn":
            status = "Cancel";
            break;
        default:
            status = "Other";
        }
    return status;
}
