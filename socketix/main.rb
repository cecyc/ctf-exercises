require "socket"

HOSTNAME = "w210.network"
PORT = 8002

s = TCPSocket.open(HOSTNAME, PORT)

parse_line = lambda do |line|
  parts = line.split
  parts.shift
  parts
end

loop do
  while line = s.gets
    puts line
    if line.empty?
      s.close
    else
      if line.include?("+")
        parts = parse_line.call(line)
        s.sendmsg("#{parts.first.to_i + parts.last.to_i}\n")          
      elsif line.include?("*")
        parts = parse_line.call(line)
        s.sendmsg("#{parts.first.to_i * parts.last.to_i}\n")
      end
    end
  end
end
