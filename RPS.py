# Ive used the markov chains algorithm abbey uses but gave it 4 moves of history giving it more states.
from RPS_game import play
def player(prev_opponent_play,
          opponent_history=[],
          play_order = [{'RRRR': 0, 'RRRP': 0, 'RRRS': 0, 'RRPR': 0, 'RRPP': 0, 'RRPS': 0, 'RRSR': 0, 'RRSP': 0, 'RRSS': 0, 'RPRR': 0, 'RPRP': 0, 'RPRS': 0, 'RPPR': 0, 'RPPP': 0, 'RPPS': 0, 'RPSR': 0, 'RPSP': 0, 'RPSS': 0, 'RSRR': 0, 'RSRP': 0, 'RSRS': 0, 'RSPR': 0, 'RSPP': 0, 'RSPS': 0, 'RSSR': 0, 'RSSP': 0, 'RSSS': 0, 'PRRR': 0, 'PRRP': 0, 'PRRS': 0, 'PRPR': 0, 'PRPP': 0, 'PRPS': 0, 'PRSR': 0, 'PRSP': 0, 'PRSS': 0, 'PPRR': 0, 'PPRP': 0, 'PPRS': 0, 'PPPR': 0, 'PPPP': 0, 'PPPS': 0, 'PPSR': 0, 'PPSP': 0, 'PPSS': 0, 'PSRR': 0, 'PSRP': 0, 'PSRS': 0, 'PSPR': 0, 'PSPP': 0, 'PSPS': 0, 'PSSR': 0, 'PSSP': 0, 'PSSS': 0, 'SRRR': 0, 'SRRP': 0, 'SRRS': 0, 'SRPR': 0, 'SRPP': 0, 'SRPS': 0, 'SRSR': 0, 'SRSP': 0, 'SRSS': 0, 'SPRR': 0, 'SPRP': 0, 'SPRS': 0, 'SPPR': 0, 'SPPP': 0, 'SPPS': 0, 'SPSR': 0, 'SPSP': 0, 'SPSS': 0, 'SSRR': 0, 'SSRP': 0, 'SSRS': 0, 'SSPR': 0, 'SSPP': 0, 'SSPS': 0, 'SSSR': 0, 'SSSP': 0, 'SSSS': 0}]):#The array of all the states you can be at like a markov chain
      if not prev_opponent_play:
          prev_opponent_play = 'RPR'
      opponent_history.append(prev_opponent_play)
#If the opponent hasnt played a move yet we impose that their last move was rock
      last_4 = "".join(opponent_history[-4:])
      if len(last_4) == 4:
          play_order[0][last_4] += 1
    #We check if there are 4 previous games played, if so we can use the markov chain to select our next play
      potential_plays = [
          last_4[-3:] + "R",
          last_4[-3:] + "S",
          last_4[-3:] + "P",
      ]#All the different plays we can make with our states

      sub_order = {
          k: play_order[0][k] #We associate the key k to the first possible play in our dictionary of plays to the k variable
          for k in potential_plays if k in play_order[0]
      }

      prediction = max(sub_order, key=sub_order.get)[-1:]

      ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
      return ideal_response[prediction]
