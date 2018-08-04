Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.

$ cat log
get_foo start 2222222100
get_foo end 2222222150
get_bar start 2222222200
get_foo start 2222222220
get_bar end 2222222230
get_foo end 2222222250
$ cat log | myprog
get_foo: average = 40
get_bar: average = 30
$

with open(“log”) as f:
    lines = f.readlines()
# function start/end time
func_times = {}
for line in lines:
    # get_foo start 2222222100
    split = line.split(“ “)
    name, msg, time = split[0], split[1], split[2]
    if name not in func_times:
        func_times[name] = {‘start’:queue, ‘times’:[]}
    if msg == ‘start’:
        func_times[name][msg].push(time)
    else:
        first_start = func_times[name][‘start’].pop()
        func_times[name][‘times’].append(int(time) - int(first_start))
for name, value in func_times.items():
    avg_time = float(sum(value[‘times’])/len(value[‘times’],2)
    print(“{}: average = {}”.format(name, avg_time))
