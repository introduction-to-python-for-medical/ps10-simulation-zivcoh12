import json
from spread_fire import spread_fire

def test_fire():
  
  with open('.tests/initial_state.json', 'r') as f:
      grid = json.load(f)
  
  with open('.tests/final_state.json', 'r') as f:
      final_grid = json.load(f)
  
  for i in range(100):
      update_grid = spread_fire(grid)
      if update_grid == grid:
          break
      grid = update_grid
  
  assert final_grid == grid
