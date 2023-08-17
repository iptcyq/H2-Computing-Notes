SELECT competitor.name, AVG(scores.score)
FROM scores
INNER JOIN competitor on competitor.id = scores.id
GROUP BY scores.id
ORDER BY competitor.name