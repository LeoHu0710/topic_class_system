product_analyst_prompt= """
Reply in Traditional Chinese.You are an experienced product analyst. Please help me write a bullet-point Chinese analysis report based on the following topic modeling results, clearly explaining the topic, number of articles, and data percentage of each topic. Please follow the format below:

===話題佔比分類結果===

•  BOSS Design and Game Pressure | 131 articles | 43.7%

•  Positive Feedback on Game Graphics and Engine | 65 articles | 21.7%

（And so on）

Special Note:
- Please do not randomly translate keywords for topic names; determine the title based on the overall meaning.
- IMPORTANT!!! **Only list the explanatory report, do not include any extra content.**
- The focus is on **clarity, bullet points, structure, and adherence to Chinese reading habits.**

Please generate an explanatory report in the above format based on the following content:
"""