#!/usr/bin/env ruby

# Read the log file name from the command line argument
file_path = ARGV[0]

# Read each line from the log file
File.open(file_path, 'r').each_line do |line|
  # Extract relevant information using regex patterns
  match_data = line.match(/\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/)

  # Output the extracted information
  if match_data
    sender = match_data[:sender].gsub('from:', '').strip
    receiver = match_data[:receiver].gsub('to:', '').strip
    flags = match_data[:flags].gsub('flags:', '').strip
    puts "#{sender},#{receiver},#{flags}"
  end
end
