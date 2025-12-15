from flask import jsonify, make_response
import dicttoxml

def response_format(data, format="json"):
    format = format.lower() if format else "json"
    
    if format == "xml":
        try:
            xml_data = dicttoxml.dicttoxml(data, attr_type=False)
            response = make_response(xml_data)
            response.headers['Content-Type'] = 'application/xml; charset=utf-8'
            return response
        except Exception as e:
            return jsonify({"error": f"XML conversion failed: {str(e)}"}), 500
    
    elif format == "json":
        return jsonify(data)
    
    else:
        return jsonify({"error": f"Unsupported format: {format}. Use 'json' or 'xml'"}), 400