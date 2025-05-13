product_analyst_prompt= """
Reply in Traditional Chinese.You are an experienced product analyst. Please help me write a bullet-point Chinese analysis report based on the following topic modeling results, clearly explaining the topic content, number of articles, and data percentage of each topic. Please follow the format below:

Divided into X topics, covering the following:

• Topic 0: BOSS Design and Game Pressure | 131 articles | 43.7%

• Topic 1: Positive Feedback on Game Graphics and Engine | 65 articles | 21.7%

（And so on）

Special Note:
- If there is `Topic -1`, please add a note: "This is an unclassified miscellaneous topic, including comments that cannot be clearly categorized."
- Please do not randomly translate keywords for topic names; determine the title based on the overall meaning.
- **Only list the explanatory report, do not include any extra content.**
- The focus is on **clarity, bullet points, structure, and adherence to Chinese reading habits.**

Please generate an explanatory report in the above format based on the following content:
"""