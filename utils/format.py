from flask import jsonify, make_response
import dicttoxml

def response_converter(data, format="json"):

    if not format:
        format = "json"
    
    format = format.lower()
    

    if format == "xml":
        xml_data = dicttoxml.dicttoxml(data)
        response = make_response(xml_data)
        response.headers['Content-Type'] = 'application/xml'
        return response
    

    if format == "json":
        return jsonify(data)
    

    return jsonify({"error": "Format not supported"}), 400