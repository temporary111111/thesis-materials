# Chapter 2 Source Verification Notes

**Project:** *Machine Learning Classification of AI-Generated and Real Text-Containing Images Using Visual Text-Region Features*  
**Audit date:** September 19, 2026  
**Audited file:** `Chapter_2_Source_to_Section_Matrix.xlsx`

## Audit result

The matrix contains 35 unique candidate sources: 33 published works and two arXiv preprints. The thematic distribution is sufficient for the planned Chapter 2 sections, including the three sources added for the systems and prototype context. No duplicate source IDs, titles, citations, or links were found. The working draft should retain the two preprints only with explicit preprint labels and should rely on peer-reviewed sources for the main methodological claims whenever possible.

## Corrections to apply in the Chapter 2 draft

1. **Matrix ID 9 — DBNet++.** Cite the journal issue as **2023**, volume 45, issue 1, pages 919–931. The article appeared online in 2022, which explains the earlier year in the matrix.
2. **Matrix ID 13 — CG-DIQA.** Replace the matrix entry with: Hongyu Li, Fan Zhu, and Junhua Qiu (2018), *CG-DIQA: No-reference document image quality assessment based on character gradient*, ICPR 2018, pp. 3622–3626, https://doi.org/10.1109/ICPR.2018.8545433. The title and author initials in the matrix are incorrect.
3. **Matrix ID 16 — NPR.** The complete author list includes **Huan Liu**: Chuangchuang Tan, Huan Liu, Yao Zhao, Shikui Wei, Guanghua Gu, Ping Liu, and Yunchao Wei.
4. **Matrix ID 20 — PatchCraft.** Retain **2023** as the preprint year because arXiv:2311.12397 was first submitted in 2023. Do not present it as peer-reviewed unless a venue version is verified before submission.
5. **Matrix ID 21 — hybrid texture and sensor-noise features.** Correct the authors to **Tao Fu, Ming Xia, and Gaobo Yang**. The author initials in the matrix are incorrect.
6. **Matrix ID 3 — AIDE.** Use **Quxiang Li**, not “O. Li,” in the final reference.
7. **Matrix ID 30 — classification measures.** The official record spells the authors as Martijn Gösgens, Anton Zhiyanov, Aleksey Tikhonov, and Liudmila Prokhorenkova.

## Verified bibliographic details added during the audit

- Bird and Lotfi (2024): *IEEE Access*, 12, 15642–15650; https://doi.org/10.1109/ACCESS.2024.3356122.
- Park and Owens (2025): CVPR 2025, pp. 8245–8257.
- Li et al. (2025): ICCV 2025, pp. 20379–20389.
- Gye et al. (2025): WACV 2025, pp. 399–408.
- Sinitsa and Fried (2024): WACV 2024, pp. 4067–4076.
- Wang et al. (2023): ICCV 2023, pp. 22445–22455.
- Ricker et al. (2024): CVPR 2024, pp. 9130–9140.
- Zhang et al. (2021): ICCV 2021, pp. 1305–1314.
- Baek et al. (2019): CVPR 2019, pp. 9365–9374.
- Epshtein et al. (2010): CVPR 2010, pp. 2963–2970; https://doi.org/10.1109/CVPR.2010.5540041.
- Chai et al. (2020): ECCV 2020, LNCS 12371, pp. 103–120; https://doi.org/10.1007/978-3-030-58574-7_7.
- Tan et al. (2023): CVPR 2023, pp. 12105–12114.
- Tan et al. (2024): CVPR 2024, pp. 28130–28139; https://doi.org/10.1109/CVPR52733.2024.02657.
- Asghar et al. (2019): *Machine Vision and Applications*, 30(7–8), 1243–1262; https://doi.org/10.1007/s00138-019-01048-2.
- Kapoor and Narayanan (2023): *Patterns*, 4(9), 100804; https://doi.org/10.1016/j.patter.2023.100804.
- Chen et al. (2024): *Artificial Intelligence Review*, 57(6), Article 137; https://doi.org/10.1007/s10462-024-10759-6.

## Scope decisions carried into the draft

- The study classifies complete images as **AI-generated** or **real/non-AI-generated**, while text regions supply the visual evidence.
- Text detection is used only for localization. Recognized words, spelling, language, semantics, and OCR transcription are excluded.
- Cross-generator, cross-dataset, social-media degradation, re-digitization, and adversarial-robustness tests are discussed as broader reliability concerns and future extensions. They are not presented as required experiments because Chapter 1 excludes them from the initial scope.
- The systems section frames the software as a thin, traceable research prototype around the fixed experimental pipeline. It does not claim production-grade MLOps, public forensic certainty, automatic ISO compliance, or a full usability study.
- The two preprints—TextFake and PatchCraft—are used cautiously and are identified as preprints in both the prose and reference list.

## Final pre-submission checks

- Recheck whether TextFake or PatchCraft has obtained a peer-reviewed venue version.
- Replace provisional conference citations with institutional APA formatting if the department prescribes a format different from APA 7.
- Match the final conceptual-framework figure number to the numbering used in the completed manuscript.
- Update future-tense method statements if Chapter 3 later fixes a specific text detector, feature formula, aggregation rule, validation scheme, or prototype technology.
