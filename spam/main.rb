# frozen_string_literal: true

require "httparty"

URL = "http://w210.network:8005/flag.txt"

loop do
  request = HTTParty.get(URL)
  if request.body != "Spam!"
    puts request.body
    puts request.headers
    break
  end
  sleep 0.1
end
