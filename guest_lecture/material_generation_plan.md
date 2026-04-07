# Guest Lecture Material Generation Plan

This plan is based only on the current repository contents and previously stated user requirements.

## Source base used for planning

Repository evidence:
- `Syllabus-scan.jpeg`
- `generate_syllabus_page_4_pdf.py`
- `syllabus-page-4.pdf`

User requirements already stated in chat:
- bachelor-level audience;
- students should be able to apply the lecture ideas to their own projects;
- fit as much syllabus-relevant content as possible;
- stay in the lecturer's expertise zone;
- be interesting to listen to;
- keep work controllable, versioned, and traceable.

## Planning principle

Separate the work into two layers:

1. **Repo-grounded content layer**
   - What the syllabus page explicitly supports.
2. **Lecture-design layer**
   - How to package that content for a bachelor audience.

## Repo-grounded lecture scope

### Direct anchor
- Topic 11: **ML-enabled IS & Evaluation Metrics**

### Adjacent supporting topics from the same syllabus page
- Topic 5: Problem Framing theories in Information Systems
- Topic 10: IS Requirements & Solution Design
- Topic 12: Integrating Field Data for IS Decisions
- Topic 14: Professional Reporting & Stakeholder Presentation

## Material package to generate next

### 1. Lecture objectives
Deliver a short file that states:
- what students should understand;
- what students should be able to do after the lecture.

### 2. Slide-by-slide outline
A versioned slide plan that covers:
1. What an ML-enabled information system is
2. Why evaluation starts from the problem, not from the metric
3. How to choose metrics by task type
4. Why model metrics are not enough
5. How students can evaluate their own projects

### 3. Speaker notes
A talk track written for live delivery in front of bachelor students.

### 4. Student project framework
A reusable checklist or canvas that students can apply to their own project:
- problem
- user
- IS context
- ML task
- metric choice
- decision consequence
- project reporting

### 5. Practical mini-activity
A short in-class exercise where students classify a project and pick evaluation metrics.

### 6. Reference log
A file that records every repo source and any later external source used in the lecture materials.

## Proposed lecture architecture

### Part 1 — Information Systems context
Use Topics 5 and 10 to frame:
- what problem is being solved;
- what the system must support;
- what requirements matter.

### Part 2 — ML-enabled IS
Use Topic 11 to explain:
- where ML enters the system;
- what prediction/decision role it plays;
- why evaluation must match the task.

### Part 3 — Evaluation metrics
Teach:
- classification metrics;
- regression metrics;
- ranking/recommendation metrics if needed;
- the difference between metric choice and business usefulness.

### Part 4 — Decision and reporting
Use Topics 12 and 14 to close the loop:
- how results support IS decisions;
- how to communicate model quality responsibly;
- how students should present their evaluation in a project.

## Output order recommended for commits

1. `docs/references/*`
2. `guest_lecture/topic_recommendation.md`
3. `guest_lecture/material_generation_plan.md`
4. `guest_lecture/lecture_objectives.md`
5. `guest_lecture/slide_outline.md`
6. `guest_lecture/speaker_notes.md`
7. `guest_lecture/student_project_framework.md`
8. `guest_lecture/practical_activity.md`
9. `references/source_log.md`

## Control requirement

Each file should state:
- whether its content is explicit repo evidence;
- or a lecture-design decision built on that evidence.
