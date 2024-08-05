"""
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

"""

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        # updated_scores = scores.copy()
        dp = [score for [score, _] in pairs]

        for pair in range(len(pairs)):
            for ipair in range(pair):
                if pairs[pair][1] >= pairs[ipair][1]:
                    dp[pair] = max(dp[pair], dp[ipair] + pairs[pair][0])
        return max(dp)