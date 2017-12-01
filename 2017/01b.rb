test = {
  '1212'     => 6,
  '1221'     => 0,
  '123425'   => 4,
  '123123'   => 12,
  '12131415' => 4,
}

c=->s{s.split('').select.with_index{|(a, e),i|s[i]==(s*2)[i+s.size/2]}.map(&:to_i).reduce(0,&:+)}

test.each do |a, b|
  puts format('%s => %s == %s => %s', a, c.call(a), b, c.call(a) == b)
end

puts c.call(File.read('01.txt').strip)
