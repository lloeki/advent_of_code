test = {
  '1122'     => 3,
  '1111'     => 4,
  '1234'     => 0,
  '91212129' => 9,
}

def captcha(str)
  (0...str.size).reduce(0) do |a, i|
    x, y = str[i..i+1].split('').map(&:to_i)
    y = str[0].to_i if y.nil?
    x == y ? a + x : a
  end
end

c=->s{captcha(s)}

c=->s{(0...s.size).reduce(0){|a,i|x,y=s[i..i+1].split('').map(&:to_i);y||=s[0].to_i;x==y ? a+x : a}}

c=->s{(s[-1]+s).gsub(/(\d)/,'\1\1')[1..-1].split(/(..)/).reduce(0){|a,e|e=~/(\d)\1/ ? a+$1.to_i : a}}
c=->s{s.split('').select.with_index{|(a, e),i|s[i]==(s*2)[i+1]}.map(&:to_i).reduce(0,&:+)}

test.each do |a, b|
  puts format('%s => %s == %s => %s', a, c.call(a), b, c.call(a) == b)
end

puts c.call(File.read('01.txt').strip)
