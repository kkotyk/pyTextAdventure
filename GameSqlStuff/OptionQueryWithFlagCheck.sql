SELECT O.* 
FROM Option O 
JOIN FrameOption FO on O.option_id = FO.option_id
LEFT JOIN FlagOption FlO on FlO.option_id = O.option_id
LEFT JOIN Flag F on FlO.flag_id = F.flag_id
WHERE FO.frame_num = 1 AND (F.value in ('test') OR FlO.flag_option_id is null);
