=begin
#An example of generating swagger via gRPC ecosystem.

#No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0
Contact: none@example.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.3.1

=end

require 'cgi'

module OpenapiClient
  class ExampleServiceApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # @param id [String] 
    # @param body [V1ExampleServiceQueryRequest] 
    # @param [Hash] opts the optional parameters
    # @return [V1ExampleServiceQueryResponse]
    def example_service_query(id, body, opts = {})
      data, _status_code, _headers = example_service_query_with_http_info(id, body, opts)
      data
    end

    # @param id [String] 
    # @param body [V1ExampleServiceQueryRequest] 
    # @param [Hash] opts the optional parameters
    # @return [Array<(V1ExampleServiceQueryResponse, Integer, Hash)>] V1ExampleServiceQueryResponse data, response status code and response headers
    def example_service_query_with_http_info(id, body, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: ExampleServiceApi.example_service_query ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling ExampleServiceApi.example_service_query"
      end
      # verify the required parameter 'body' is set
      if @api_client.config.client_side_validation && body.nil?
        fail ArgumentError, "Missing the required parameter 'body' when calling ExampleServiceApi.example_service_query"
      end
      # resource path
      local_var_path = '/v1/example/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] || @api_client.object_to_http_body(body) 

      # return_type
      return_type = opts[:return_type] || 'V1ExampleServiceQueryResponse' 

      # auth_names
      auth_names = opts[:auth_names] || ['ApiKeyAuth', 'OAuth2']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: ExampleServiceApi#example_service_query\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end