-- 1. Rank categories by average views
SELECT category_id, COUNT(*) AS videos, AVG(views) AS avg_views
FROM youtube
GROUP BY category_id
ORDER BY avg_views DESC;

-- 2. Top 10 channels with most trending videos
SELECT channel_title, COUNT(*) AS trending_count
FROM youtube
GROUP BY channel_title
ORDER BY trending_count DESC
LIMIT 10;

-- 3. Likes-to-views ratio per category
SELECT category_id,
       AVG(CASE WHEN views > 0 THEN likes * 1.0 / views END) AS avg_like_ratio
FROM youtube
GROUP BY category_id
ORDER BY avg_like_ratio DESC;

-- 4. Videos with maximum trending duration
SELECT video_id, title, channel_title, MAX(trending_days) AS days
FROM youtube
GROUP BY video_id
ORDER BY days DESC
LIMIT 10;

-- 5. Extreme engagement cases
SELECT video_id, title, views, likes, comment_count,
       (likes * 1.0 / views) AS like_ratio,
       (comment_count * 1.0 / likes) AS comments_to_likes
FROM youtube
ORDER BY like_ratio DESC
LIMIT 10;
