notification :off

guard 'shell' do
  watch(/^test.*.py$/) {|m| `nosetests --with-yanc test/unit` }
end
