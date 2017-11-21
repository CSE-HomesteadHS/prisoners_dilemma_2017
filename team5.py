# -*- coding: utf-8 -*-
team_name = 'Коммунисты'
strategy_name = 'return b'
strategy_description = 'use communism to win'
def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history or len(their_history)>100: 
        return 'b'
    else:
        return 'b'
    
    
    