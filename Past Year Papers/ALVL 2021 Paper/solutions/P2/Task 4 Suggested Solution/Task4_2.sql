SELECT competitor.name, scores.score
FROM competitor
INNER JOIN scores on competitor.id = scores.id
WHERE score > 0 and round = 1
ORDER BY score DESC