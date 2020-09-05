function sourceDataTypeOnChange() {
    let sourceDataType = $("#sourceDataType").val();
    $("#targetDataType").attr("disabled", false);
    if (sourceDataType === "1") {
        $("#targetDataType").val("2");
    } else if (sourceDataType === "2") {
        $("#targetDataType").val("1");
    } else {
        $("#targetDataType").val("0");
    }
    $("#targetDataType").attr("disabled", true);
}

function convertData() {
    let route = "";
    let sourceText = btoa($("#sourceText").val());
    let sourceDataType = parseInt($("#sourceDataType").val());
    let targetDataType = parseInt($("#targetDataType").val());

    if (sourceDataType === 1 && targetDataType === 2) {
        route = "/JsonToCsv";
    } else if (sourceDataType === 2 && targetDataType === 1) {
        route = "/CsvToJson";
    } else {
        alert("Source and target data types must be different.");
        return;
    }

    let obj = {
        "sourceB64": sourceText, 
        "sourceType": sourceDataType, 
        "targetType": targetDataType
    }
    
    $.ajax({
        url: route, 
        type: "POST", 
        data: JSON.stringify(obj),
        contentType: "application/json; charset=utf-8",
        dataType: "json", 
        success: successFunc
    });

    function successFunc(data, requestText, jqXhr) {
        let message = ""

        if (requestText === "success") {
            message = atob(data["responseString"]);
        } else {
            message = "An error occurred. Please try again . . ."
        }

        $("#targetText").val(message);
    }
}

$("#sourceDataType").change(sourceDataTypeOnChange);
$("#convertButton").click(convertData);