"""
Cookie Clicker Simulator
"""

import simpleplot
import math
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._cps = 1.0
        #time,item/None, the item cost,total cookies
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "ClickerState: time " + str(self._current_time) + " current cookie " + str(self._current_cookies)+ " total " + str(self._total_cookies)+ " cps " + str(self._cps)+ " history " + str(self._history)
        
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        else:
            return math.ceil((cookies - self._current_cookies) / self._cps)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            return
        else:
            self._current_time += time
            self._current_cookies += self._cps * time
            self._total_cookies += self._cps * time
            
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._cps += additional_cps
            #time,item/None, the item cost,total cookies
            self._history.append((self._current_time, item_name, cost, self._total_cookies))
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    info = build_info.clone()
    state = ClickerState()
    # Replace with your code
    while state.get_time() <= duration:
        time_left = duration - state.get_time()
        item_next = strategy(state.get_cookies(), state.get_cps(), state.get_history(), time_left, info)
        if item_next == None or state.time_until(info.get_cost(item_next)) > time_left :
            state.wait(duration - state.get_time())
            break
        time_next = state.time_until(info.get_cost(item_next))
        state.wait(time_next)
        state.buy_item(item_next, info.get_cost(item_next),info.get_cps(item_next))
        info.update_item(item_next)
    return state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    result = None
    result_cost = float('inf')
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        item_time = math.ceil((item_cost - cookies) / cps)
        print item_cost
        if result_cost >= item_cost and (cookies >= item_cost or item_time <= time_left) :
            result = item
            result_cost = item_cost
    return result

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    result = None
    result_cost = 0.0
    for item in  build_info.build_items():
        item_cost = build_info.get_cost(item)
        item_time = math.ceil((item_cost - cookies) / cps)
        if result_cost <= item_cost and (cookies >= item_cost or item_time <= time_left) :
            result = item
            result_cost = item_cost
    return result

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    cps_advance = 0.0
    result = None
    for item in  build_info.build_items():
        item_cost = build_info.get_cost(item)
        item_time = math.ceil((item_cost - cookies) / cps)
        item_cps_advance = build_info.get_cps(item) / item_cost
        if item_cps_advance >= cps_advance and (cookies >= item_cost or item_time <= time_left) :
            result = item
            cps_advance = item_cps_advance
    return result
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001], 'Grandma': [100.0, 0.5]}, 1.15), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", 400.0, strategy_cheap)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    

