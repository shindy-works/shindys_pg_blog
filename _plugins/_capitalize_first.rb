require 'liquid'
require 'uri'

# Capitalize all words of the input
module Jekyll
  module CapitalizeFirst
    def capitalize_first(words)
      if not words.nil? then
        return words.split(' ').map(&:capitalize).join(' ')
      end
      return words
    end
  end
end

Liquid::Template.register_filter(Jekyll::CapitalizeFirst)