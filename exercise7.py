
runner_ids = [1,2,3] # TODO: Prompt the user to specify how many racers

print(f"How many racers?")
runner_ids = range(int(input()))


def collect_runner_info(id):
  print(f"How far did person {id} run (in metres)?")
  distance = float(input())
  print(f"How long (in minutes) did person 1 run take to run {distance} metres?")
  mins = float(input())
  speed = distance / (mins * 60)
  return {
    "id": id,
    "speed": speed
  }


results = []

for id in runner_ids:
  result = collect_runner_info(id)
  results.append(result)

def by_speed(runner):
  return runner['speed']

sorted_results = sorted(results, key=by_speed, reverse=True)

print(sorted_results)

winner = sorted_results[0]

print(f"Person {winner['id']} was the fastest at {winner['speed']} m/s")
print("Well done everyone!")