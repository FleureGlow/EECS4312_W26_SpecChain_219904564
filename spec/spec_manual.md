# Manual Specification for MindDoc

## Overview
This specification was manually derived from the personas created from grouped user reviews. It describes the system behaviors and supports needed by the identified user groups.

# Requirement ID: R1
- Description: The system shall clearly indicate which features are free and which features require payment before the user begins using those features.
- Source Persona: P1 (Mya)
- Traceability: Derived from review group G1
- Acceptance Criteria: Free and premium features are visually distinguishable on the main interface; premium-only features display a label before the user interacts with them; the user is not required to complete multiple steps before learning that a feature is paid.

# Requirement ID: R2
- Description: The system shall provide a useful free version that allows users to track mood and access basic mental health support without requiring immediate payment.
- Source Persona: P1 (Mya)
- Traceability: Derived from review group G1
- Acceptance Criteria: A user can log mood entries without a subscription; a user can view basic mood history without subscribing; a user can complete at least one meaningful self-help activity or insight flow without payment.

# Requirement ID: R3
- Description: The system shall provide users with summaries and insights based on their recorded mood data over time.
- Source Persona: P2 (Mick)
- Traceability: Derived from review group G2
- Acceptance Criteria: The user can view a summary of mood entries over a defined period; the summary includes identifiable trends or patterns from recorded entries; the insight view is available after sufficient mood data has been collected.

# Requirement ID: R4
- Description: The system shall support regular self-reflection by prompting users with structured mental health questions and journaling tasks.
- Source Persona: P2 (Mick)
- Traceability: Derived from review group G2
- Acceptance Criteria: The user receives reflection prompts at scheduled points in time; the user can submit written reflections linked to mood check-ins; previous reflections remain viewable in the user’s history.

# Requirement ID: R5
- Description: The system shall operate without frequent crashes or blocking failures during core tasks such as login, check-in, and viewing results.
- Source Persona: P3 (Aysha)
- Traceability: Derived from review group G3
- Acceptance Criteria: The user can open the app successfully; the user can complete a check-in without the app closing unexpectedly; the user can access saved results without encountering a blocking failure.

# Requirement ID: R6
- Description: The system shall provide essential usability settings that improve access and convenience, such as language support and secure access options.
- Source Persona: P3 (Aysha)
- Traceability: Derived from review group G3
- Acceptance Criteria: The user can change the application language from settings; the user can enable a secure access option like a PIN or biometric lock; settings changes are saved for future sessions.

# Requirement ID: R7
- Description: The system shall clearly explain what personal and health-related data is collected, why it is collected, and how it is used before consent is requested.
- Source Persona: P4 (Gabriel)
- Traceability: Derived from review group G4
- Acceptance Criteria: The user is shown a readable privacy explanation before account creation is completed; the explanation states what data is collected and for what purpose; the user can decline consent and exit without being forced deeper into onboarding.

# Requirement ID: R8
- Description: The system shall provide users with control over account creation, stored personal data, and privacy-related settings.
- Source Persona: P4 (Gabriel)
- Traceability: Derived from review group G4
- Acceptance Criteria: The user can view privacy-related settings after account creation; the user can request deletion of stored account data; the user can review whether sensitive entries are stored in the account.

# Requirement ID: R9
- Description: The system shall provide supportive guidance for users experiencing distress, anxiety, depression, or other difficult emotional states.
- Source Persona: P5 (Priya)
- Traceability: Derived from review group G5
- Acceptance Criteria: The user can access coping guidance from within the app; emotional support content is reachable within a small number of clicks from the home or check-in flow; support content is written in a calm and non-judgmental tone.

# Requirement ID: R10
- Description: The system shall provide accessible crisis support options when user responses indicate potential self-harm, suicidal ideation, or severe emotional distress.
- Source Persona: P5 (Priya)
- Traceability: Derived from review group G5
- Acceptance Criteria: If a user reports a high-risk mental health state, the system displays crisis support options immediately; crisis support options include at least one direct action method such as call, text, or external contact; crisis support information remains visible until dismissed by the user.

# Requirement ID: R11
- Description: The system shall provide support pathways that consider users with different accessibility and communication needs.
- Source Persona: P5 (Priya)
- Traceability: Derived from review group G5
- Acceptance Criteria: Crisis or support contact information includes more than one communication channel where possible; the system does not assume all users can make voice calls; support guidance is understandable without requiring advanced mental health knowledge.

# Requirement ID: R12
- Description: The system shall tailor prompts, questions, or follow-up insights based on the user’s previous responses and recorded mood patterns.
- Source Persona: P2 (Mick)
- Traceability: Derived from review group G2
- Acceptance Criteria: The system changes future prompts based on prior user input; repetitive prompts are reduced when recent responses are similar; the user receives follow-up content that reflects their tracked concerns or goals.

## Traceability Summary
- P1 → R1, R2
- P2 → R3, R4, R12
- P3 → R5, R6
- P4 → R7, R8
- P5 → R9, R10, R11
