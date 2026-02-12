# 🧪 Sample Test Inputs – AI Immigration Assistant

Use these inputs in the form to test the system.

---

## 1. Student Visa – Canada
Country: Canada  
Visa Type: Student  
Profile: Indian student after 12th science  

Expected:
Clean structured visa guidance.

---

## 2. Tourist Visa – USA
Country: USA  
Visa Type: Tourist  
Profile: Indian family visiting for 2 weeks  

Expected:
Tourist visa steps + documents.

---

## 3. Work Visa – Germany
Country: Germany  
Visa Type: Work  
Profile: Software engineer with 2 years experience  

Expected:
Work visa eligibility + steps.

---

## 4. Student Visa – UK
Country: United Kingdom  
Visa Type: Student  
Profile: BCom graduate applying for MBA  

Expected:
Student visa checklist.

---

## 5. Work Visa – Australia
Country: Australia  
Visa Type: Work  
Profile: Mechanical engineer fresher  

Expected:
Work visa process.

---

## Edge Case Tests

### 6. Lowercase input
Country: canada  
Visa Type: student  
Profile: diploma student  

---

### 7. Long profile
Country: USA  
Visa Type: Student  
Profile: Indian student with IELTS 7.5 applying for MS in Data Science with scholarship  

---

### 8. Empty fields
Country:  
Visa Type: Student  
Profile: Student  

Expected:
Show validation message.

---

### 9. Invalid country
Country: Atlantis  
Visa Type: Work  
Profile: Engineer  

Expected:
Still generate general guidance.

---

### 10. Tourist visa Japan
Country: Japan  
Visa Type: Tourist  
Profile: Solo traveler  

Expected:
Tourist visa guidance.
