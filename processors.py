import os
import base64
import json
import io
import csv
from flask import Flask, jsonify, redirect, render_template, request
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError


def JsonToCsvProcessor(request):
    try:
        sourceString = base64.b64decode(request.json["sourceB64"]).decode()

        if not sourceString or sourceString == "":
            return errorResponse("Source string cannot be empty", 400)

        sourceObj = json.loads(sourceString)
        fieldNames = []
        responseString = ""

        if isinstance(sourceObj, list):
            for key in sourceObj[0].keys():
                fieldNames.append(key)
        elif isinstance(sourceObj, dict):
            for key in sourceObj.keys():
                fieldNames.append(key)
        else: 
            return errorResponse("Source string must be in JSON format", 400)

        with io.StringIO() as outString:
            writer = csv.DictWriter(outString, fieldnames=fieldNames)
            writer.writeheader()

            if isinstance(sourceObj, list):
                for obj in sourceObj:
                    writer.writerow(obj)
            elif isinstance(sourceObj, dict):
                writer.writerow(sourceObj)
            
            responseString = outString.getvalue()

        responseObj = {
            "dataType": request.json["targetType"], 
            "responseString": base64.b64encode(responseString.encode()).decode()
        }

        return jsonify(responseObj)
    except:
        return errorResponse("An unexpected error occurred", 500)


def CsvToJsonProcessor(request):
    sourceString = base64.b64decode(request.json["sourceB64"]).decode()

    if not sourceString or sourceString == "":
        return errorResponse("Source string cannot be empty", 400)

    with io.StringIO(sourceString) as stringBuffer:
        reader = csv.DictReader(stringBuffer)
        fieldNames = reader.fieldnames

        responseList = []
        for row in reader:            
            responseList.append(row)
        
        if len(responseList) == 0:
            return errorResponse("Number of rows parsed in teh CSV string equals zero", 400)
        elif len(responseList) == 1:
            responseList = responseList[0]

    responseObj = {
        "dataType": request.json["targetType"],
        "responseString": base64.b64encode(json.dumps(responseList).encode()).decode()
    }

    return jsonify(responseObj)


def errorResponse(message, httpCode):
    responseObj = {
        "title": "An error occurred", 
        "message": message
    }
    return (jsonify(responseObj), httpCode)