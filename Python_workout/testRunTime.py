from runTiming import run_timing

def test_run():
    running = run_timing("running time (minutes):", 15.25)
    assert run_timing == "Average running time: 15.25"
    