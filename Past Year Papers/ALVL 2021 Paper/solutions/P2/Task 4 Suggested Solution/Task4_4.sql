SELECT competitor.name, SUM(scores.score), SUM(scores.score) > 250
FROM scores
INNER JOIN competitor on competitor.id = scores.id
GROUP BY scores.id
ORDER BY SUM(scores.score) DESC