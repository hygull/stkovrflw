teststruct = struct('a',3,'b',5,'c',9)

fields = fieldnames(teststruct)

for i=1:numel(fields)
  teststruct.(fields{i})
end