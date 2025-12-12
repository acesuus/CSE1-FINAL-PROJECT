from flask import jsonify, make_response
import dicttoxml

def response_format(data, fmt="json"):
    fmt = fmt.lower() if fmt else "json"
    
    if fmt == "xml":
        try:
            xml_data = dicttoxml.dicttoxml(data, attr_type=False)
            response = make_response(xml_data)
            response.headers['Content-Type'] = 'application/xml; charset=utf-8'
            return response
        except Exception as e:
            return jsonify({"error": f"XML conversion failed: {str(e)}"}), 500
    
    elif fmt == "json":
        return jsonify(data)
    
    else:
        return jsonify({"error": f"Unsupported format: {fmt}. Use 'json' or 'xml'"}), 400