require 'sinatra'
require 'json'

get '/' do
  content_type :json
  { :celsius => 15.6 }.to_json
end
