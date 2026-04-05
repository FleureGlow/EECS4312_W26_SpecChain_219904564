# Manual Specification for MindDoc

## Overview
This specification was manually derived from the personas created from grouped user reviews. It describes the system behaviors and supports needed by the identified user groups.

---

## Requirement R1
**Requirement ID:** R1  
**Title:** Transparency for feature access information  
**Originating Persona:** P1 (Mya)  
**Description:** The system shall clearly indicate which features are free and which features require payment before the user begins using those features.  

**Acceptance Criteria:**
- Free and premium features are visually distinguishable on the main interface.
- Premium-only features display a label before the user interacts with them.
- The user is not required to complete multiple steps before learning that a feature is paid.

---

## Requirement R2
**Requirement ID:** R2  
**Title:** Affordable/free mental health tracking  
**Originating Persona:** P1 (Mya)  
**Description:** The system shall provide a useful free version that allows users to track mood and access basic mental health support without requiring immediate payment.  

**Acceptance Criteria:**
- A user can log mood entries without a subscription.
- A user can view basic mood history without subscribing.
- A user can complete at least one meaningful self-help activity or insight flow without payment.

---

## Requirement R3
**Requirement ID:** R3  
**Title:** Meaningful mood tracking insights  
**Originating Persona:** P2 (Mick)  
**Description:** The system shall provide users with summaries and insights based on their recorded mood data over time.  

**Acceptance Criteria:**
- The user can view a summary of mood entries over a defined period.
- The summary includes identifiable trends or patterns from recorded entries.
- The insight view is available after sufficient mood data has been collected.

---

## Requirement R4
**Requirement ID:** R4  
**Title:** Guided reflection support  
**Originating Persona:** P2 (Mick)  
**Description:** The system shall support regular self-reflection by prompting users with structured mental health questions and journaling tasks.  

**Acceptance Criteria:**
- The user receives reflection prompts at scheduled points in time.
- The user can submit written reflections linked to mood check-ins.
- Previous reflections remain viewable in the user’s history.

---

## Requirement R5
**Requirement ID:** R5  
**Title:** Reliable application   
**Originating Persona:** P3 (Aysha)  
**Description:** The system shall operate without frequent crashes or blocking failures during core tasks such as login, check-in, and viewing results.  

**Acceptance Criteria:**
- The user can open the app successfully.
- The user can complete a check-in without the app closing unexpectedly.
- The user can access saved results without encountering a blocking failure.

---

## Requirement R6
**Requirement ID:** R6  
**Title:** Basic accessibility and usability settings  
**Originating Persona:** P3 (Aysha)  
**Description:** The system shall provide essential usability settings that improve access and convenience, such as language support and secure access options.  

**Acceptance Criteria:**
- The user can change the application language from settings.
- The user can enable a secure access option like a PIN or biometric lock.
- Settings changes are saved for future sessions.

---

## Requirement R7
**Requirement ID:** R7  
**Title:** Privacy and consent transparency  
**Originating Persona:** P4 (Gabriel)  
**Description:** The system shall clearly explain what personal and health-related data is collected, why it is collected, and how it is used before consent is requested.  

**Acceptance Criteria:**
- The user is shown a readable privacy explanation before account creation is completed.
- The explanation states what data is collected and for what purpose.
- The user can decline consent and exit without being forced deeper into onboarding.

---

## Requirement R8
**Requirement ID:** R8  
**Title:** Trustworthy account and data controls  
**Originating Persona:** P4 (Gabriel)  
**Description:** The system shall provide users with control over account creation, stored personal data, and privacy-related settings.  

**Acceptance Criteria:**
- The user can view privacy-related settings after account creation.
- The user can request deletion of stored account data.
- The user can review whether sensitive entries are stored in the account.

---

## Requirement R9
**Requirement ID:** R9  
**Title:** Support for emotionally vulnerable users  
**Originating Persona:** P5 (Priya)  
**Description:** The system shall provide supportive guidance for users experiencing distress, anxiety, depression, or other difficult emotional states.  

**Acceptance Criteria:**
- The user can access coping guidance from within the app.
- Emotional support content is reachable within a small number of clicks from the home or check-in flow.
- Support content is written in a calm and non-judgmental tone.

---

## Requirement R10
**Requirement ID:** R10  
**Title:** Crisis-response signposting  
**Originating Persona:** P5 (Priya)  
**Description:** The system shall provide accessible crisis support options when user responses indicate potential self-harm, suicidal ideation, or severe emotional distress.  

**Acceptance Criteria:**
- If a user reports a high-risk mental health state, the system displays crisis support options immediately.
- Crisis support options include at least one direct action method such as call, text, or external contact.
- Crisis support information remains visible until dismissed by the user.

---

## Requirement R11
**Requirement ID:** R11  
**Title:** Inclusive support options  
**Originating Persona:** P5 (Priya)  
**Description:** The system shall provide support pathways that consider users with different accessibility and communication needs.  

**Acceptance Criteria:**
- Crisis or support contact information includes more than one communication channel where possible.
- The system does not assume all users can make voice calls.
- Support guidance is understandable without requiring advanced mental health knowledge.

---

## Requirement R12
**Requirement ID:** R12  
**Title:** Personalized and relevant prompts  
**Originating Persona:** P2 (Mick)  
**Description:** The system shall tailor prompts, questions, or follow-up insights based on the user’s previous responses and recorded mood patterns.  

**Acceptance Criteria:**
- The system changes future prompts based on prior user input.
- Repetitive prompts are reduced when recent responses are similar.
- The user receives follow-up content that reflects their tracked concerns or goals.

---

## Traceability Summary
- P1 → R1, R2
- P2 → R3, R4, R12
- P3 → R5, R6
- P4 → R7, R8
- P5 → R9, R10, R11
