require 'liquid'
require 'uri'

# Capitalize all words of the input
module Jekyll
  module CapitalizeFirst
    def capitalize_first(words)
      return words.split(' ').map(&:capitalize).join(' ')
    end
  end
end

Liquid::Template.register_filter(Jekyll::CapitalizeFirst)