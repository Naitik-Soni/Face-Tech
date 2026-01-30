## ✅ Functional Requirements (FR)

These define what the system must do.

---

### FR-1. User & Identity Management

**The system shall:**
- Allow adding a user (student / employee)
- Allow removing or deactivating a user
- Assign a unique system ID per user
- Support enrolling one or multiple face samples per user
- Store user metadata (name, role, department, etc.)

📌 **Notes:** Face enrollment ≠ attendance. Enrollment is an explicit admin action.

---

### FR-2. Face Enrollment

**The system shall:**
- Accept one or more images per user during enrollment
- Detect exactly one face per enrollment image
- Reject images with:
    - no face
    - multiple faces
    - poor quality (blur / too small face)
- Generate and store normalized face embeddings
- Support re-enrollment / update of face data

📌 **Note:** This guarantees recognition quality later.

---

### FR-3. Multi-Mode Image Ingestion

**The system shall support multiple input modes:**
- Single image upload (classroom / batch)
- Static camera snapshot (office entry / exit)
- Intentional user capture (user stands facing camera)

**All modes must:**
- Normalize their input into one image per request
- Attach metadata (timestamp, mode, camera_id)

📌 **Note:** Backend must not depend on mode-specific logic.

---

### FR-4. Face Recognition

**For each received image, the system shall:**
- Detect zero or more faces
- Independently process each detected face
- Generate embeddings for each face
- Match embeddings against enrolled users
- Return:
    - matched user ID (if above threshold)
    - confidence score
    - "unknown" if no match

📌 **Note:** Recognition ≠ attendance decision.

---

### FR-5. Attendance Marking Logic

**The system shall:**
- Mark attendance only for recognized users
- Enforce one attendance record per user per day
- Prevent duplicate marking
- Support configurable attendance windows (optional)
- Store:
    - date
    - time
    - confidence score
    - source metadata

📌 **Note:** Attendance rules are business logic, not ML.

---

### FR-6. Multi-Face Handling

**The system shall:**
- Handle multiple faces in a single image
- Process each face independently
- Mark attendance for all valid recognized users
- Ignore unknown or low-confidence faces

📌 **Note:** Required for schools / colleges.

---

### FR-7. Audit & Observability

**The system shall:**
- Log every recognition attempt
- Store failed recognition events (no match / low confidence)
- Maintain traceability:
    - image → recognition → attendance
- Allow querying attendance history

📌 **Note:** Mandatory for enterprise acceptance.

---

### FR-8. External Integration (Optional, Later)

**The system should:**
- Expose APIs for external systems (HR / LMS)
- Allow exporting attendance data

---

## ⚙️ Non-Functional Requirements (NFR)

These define how well the system must behave.

---

### NFR-1. Performance & Latency

- Single image recognition response: ≤ 200 ms (target)
- Multi-face image: ≤ 500 ms (reasonable)
- Must support concurrent requests

📌 **Note:** This drives architecture decisions later.

---

### NFR-2. Scalability

**Support:**
- 100 → 10,000+ enrolled users
- 1 → many cameras
- Horizontal scalability for backend services
- No hard coupling to a single camera or location

---

### NFR-3. Accuracy & Reliability

- Use embedding-based similarity, not classification
- Threshold must be configurable
- System must prefer false negatives over false positives
- Attendance must never be auto-marked for low confidence matches

📌 **Note:** This is how enterprises avoid legal trouble.

---

### NFR-4. Availability & Fault Tolerance

**System must handle:**
- no face detected
- multiple faces during enrollment
- corrupted images
- Failure of recognition must not crash the system
- Graceful error responses required

---

### NFR-5. Security

- Secure APIs (auth later)
- No raw images stored by default (configurable)
- Embeddings treated as sensitive data
- Access-controlled user management

---

### NFR-6. Privacy & Compliance (Critical)

- Stateless recognition pipeline
- No identity persistence across frames
- No tracking
- Clear separation of:
    - capture
    - recognition
    - attendance

📌 **Note:** This is why your design is enterprise-friendly.

---

### NFR-7. Maintainability & Extensibility

- Modular services
- Clear separation of ML and business logic
- New input modes must not affect backend
- Models should be replaceable (ArcFace → AdaFace etc.)

---

### NFR-8. Observability & Debugging

- Structured logs
- Confidence scores stored
- Ability to analyze:
    - false matches
    - rejection rates
    - system latency

