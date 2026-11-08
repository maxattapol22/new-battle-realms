# Prompt ท่าโจมตี 40 ภาพ (5 ตัวละคร × 8 ทิศ)

## ขั้นตอนทั้งหมด (ทำตามลำดับ)

1. เปิด Grok แล้วแนบภาพอ้างอิง 2 ภาพ: `assets/dragon/<ตัวละคร>.png` (ภาพเต็มตัว) และ `assets/dragon/facing/<ตัวละคร>/<ทิศ>.png` (ภาพมุมเดียวกับที่จะวาด ช่วยให้มุมหันถูก)
2. คัดลอก prompt ของภาพนั้นจากไฟล์นี้ไปวาง
3. ดูผลก่อนเซฟ: ต้องมี 4 ท่า ตัวไม่ชนกัน พื้นชมพูล้วน อาวุธถูก (หัวหน้านักรบต้องเป็นง้าวใบจันทร์เสี้ยว ไม่ใช่หอก) ถ้าไม่ผ่านให้สั่งวาดใหม่
4. เซฟภาพไว้ที่โฟลเดอร์ `grok/` ในเกม ตั้งชื่อตามที่เขียนไว้ เช่น `grok/chief_s.png`
5. เปิด Command Prompt (หน้าต่างพิมพ์คำสั่ง) ในโฟลเดอร์ New Battle Realms แล้วรันคำสั่งที่เขียนใต้ prompt
6. **ภาพแรก (chief s) ให้หยุดแล้วบอก Claude ก่อน** จะได้ตรวจเฟรมว่าตัดภาพ ย่อขนาด และวางเท้าถูกไหม ก่อนทำอีก 39 ภาพ
7. ทำครบแล้วรัน `python tools/import_attack.py --check` ต้องขึ้นครบ 8/8 ทุกตัว
8. เซฟขึ้น GitHub: `git add assets` → `git commit -m "Add attack animations"` → `git push` (ต้อง add ทั้ง `assets` เพราะคำสั่งในข้อ 5 สร้าง atlas ใหม่ใน `assets/dragon/atlas/` กับ `assets/sprites.js` ด้วย ถ้าไม่ add เกมบนเว็บจะยังพุ่งตัวแบบเดิม) (แนะนำให้ทำทุกครั้งที่จบหนึ่งตัวละคร จะได้ไม่เสียงานถ้าเครื่องมีปัญหา)

ลำดับ: chief s ก่อน → ตรวจ → chief ที่เหลือ → spear → archer → elite → leader

## chief — หัวหน้าหมู่บ้าน (มือเปล่า)

### 1. chief / s  →  `grok/chief_s.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing facing the camera. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/s.png`  
รัน: `python tools/import_attack.py grok/chief_s.png chief s`

### 2. chief / sw  →  `grok/chief_sw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's left. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/sw.png`  
รัน: `python tools/import_attack.py grok/chief_sw.png chief sw`

### 3. chief / w  →  `grok/chief_w.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing left. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/w.png`  
รัน: `python tools/import_attack.py grok/chief_w.png chief w`

### 4. chief / nw  →  `grok/chief_nw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-left. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/nw.png`  
รัน: `python tools/import_attack.py grok/chief_nw.png chief nw`

### 5. chief / n  →  `grok/chief_n.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing back view. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/n.png`  
รัน: `python tools/import_attack.py grok/chief_n.png chief n`

### 6. chief / ne  →  `grok/chief_ne.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-right. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/ne.png`  
รัน: `python tools/import_attack.py grok/chief_ne.png chief ne`

### 7. chief / e  →  `grok/chief_e.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing right. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/e.png`  
รัน: `python tools/import_attack.py grok/chief_e.png chief e`

### 8. chief / se  →  `grok/chief_se.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's right. Frame 1: draws right palm back, weight on back foot. Frame 2: steps forward with an open-palm strike. Frame 3: arm fully extended, robe sleeves flowing. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/chief.png` + `assets/dragon/facing/chief/se.png`  
รัน: `python tools/import_attack.py grok/chief_se.png chief se`

## spear — ทหารหอก

### 9. spear / s  →  `grok/spear_s.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing facing the camera. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/s.png`  
รัน: `python tools/import_attack.py grok/spear_s.png spear s`

### 10. spear / sw  →  `grok/spear_sw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's left. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/sw.png`  
รัน: `python tools/import_attack.py grok/spear_sw.png spear sw`

### 11. spear / w  →  `grok/spear_w.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing left. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/w.png`  
รัน: `python tools/import_attack.py grok/spear_w.png spear w`

### 12. spear / nw  →  `grok/spear_nw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-left. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/nw.png`  
รัน: `python tools/import_attack.py grok/spear_nw.png spear nw`

### 13. spear / n  →  `grok/spear_n.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing back view. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/n.png`  
รัน: `python tools/import_attack.py grok/spear_n.png spear n`

### 14. spear / ne  →  `grok/spear_ne.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-right. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/ne.png`  
รัน: `python tools/import_attack.py grok/spear_ne.png spear ne`

### 15. spear / e  →  `grok/spear_e.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing right. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/e.png`  
รัน: `python tools/import_attack.py grok/spear_e.png spear e`

### 16. spear / se  →  `grok/spear_se.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's right. Frame 1: pulls the spear back with both hands, tip aimed forward. Frame 2: lunges forward thrusting the spear. Frame 3: full extension, spear fully forward. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/spear.png` + `assets/dragon/facing/spear/se.png`  
รัน: `python tools/import_attack.py grok/spear_se.png spear se`

## archer — นักธนู

### 17. archer / s  →  `grok/archer_s.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing facing the camera. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/s.png`  
รัน: `python tools/import_attack.py grok/archer_s.png archer s`

### 18. archer / sw  →  `grok/archer_sw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's left. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/sw.png`  
รัน: `python tools/import_attack.py grok/archer_sw.png archer sw`

### 19. archer / w  →  `grok/archer_w.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing left. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/w.png`  
รัน: `python tools/import_attack.py grok/archer_w.png archer w`

### 20. archer / nw  →  `grok/archer_nw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-left. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/nw.png`  
รัน: `python tools/import_attack.py grok/archer_nw.png archer nw`

### 21. archer / n  →  `grok/archer_n.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing back view. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/n.png`  
รัน: `python tools/import_attack.py grok/archer_n.png archer n`

### 22. archer / ne  →  `grok/archer_ne.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-right. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/ne.png`  
รัน: `python tools/import_attack.py grok/archer_ne.png archer ne`

### 23. archer / e  →  `grok/archer_e.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing right. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/e.png`  
รัน: `python tools/import_attack.py grok/archer_e.png archer e`

### 24. archer / se  →  `grok/archer_se.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's right. Frame 1: nocks an arrow, bow raised. Frame 2: draws the string fully to the cheek. Frame 3: release, string snapped forward, hand open behind, no arrow visible. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/archer.png` + `assets/dragon/facing/archer/se.png`  
รัน: `python tools/import_attack.py grok/archer_se.png archer se`

## elite — นักรบมังกร

### 25. elite / s  →  `grok/elite_s.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing facing the camera. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/s.png`  
รัน: `python tools/import_attack.py grok/elite_s.png elite s`

### 26. elite / sw  →  `grok/elite_sw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's left. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/sw.png`  
รัน: `python tools/import_attack.py grok/elite_sw.png elite sw`

### 27. elite / w  →  `grok/elite_w.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing left. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/w.png`  
รัน: `python tools/import_attack.py grok/elite_w.png elite w`

### 28. elite / nw  →  `grok/elite_nw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-left. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/nw.png`  
รัน: `python tools/import_attack.py grok/elite_nw.png elite nw`

### 29. elite / n  →  `grok/elite_n.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing back view. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/n.png`  
รัน: `python tools/import_attack.py grok/elite_n.png elite n`

### 30. elite / ne  →  `grok/elite_ne.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-right. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/ne.png`  
รัน: `python tools/import_attack.py grok/elite_ne.png elite ne`

### 31. elite / e  →  `grok/elite_e.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing right. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/e.png`  
รัน: `python tools/import_attack.py grok/elite_e.png elite e`

### 32. elite / se  →  `grok/elite_se.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's right. Frame 1: raises the crescent-blade guandao overhead with both hands. Frame 2: diagonal downward slash. Frame 3: follow-through, blade low near the ground. Frame 4: back to the neutral standing pose. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/elite.png` + `assets/dragon/facing/elite/se.png`  
รัน: `python tools/import_attack.py grok/elite_se.png elite se`

## leader — หัวหน้านักรบ

### 33. leader / s  →  `grok/leader_s.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing facing the camera. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/s.png`  
รัน: `python tools/import_attack.py grok/leader_s.png leader s`

### 34. leader / sw  →  `grok/leader_sw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's left. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/sw.png`  
รัน: `python tools/import_attack.py grok/leader_sw.png leader sw`

### 35. leader / w  →  `grok/leader_w.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing left. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/w.png`  
รัน: `python tools/import_attack.py grok/leader_w.png leader w`

### 36. leader / nw  →  `grok/leader_nw.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-left. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/nw.png`  
รัน: `python tools/import_attack.py grok/leader_nw.png leader nw`

### 37. leader / n  →  `grok/leader_n.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing back view. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/n.png`  
รัน: `python tools/import_attack.py grok/leader_n.png leader n`

### 38. leader / ne  →  `grok/leader_ne.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter back view, facing up-right. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/ne.png`  
รัน: `python tools/import_attack.py grok/leader_ne.png leader ne`

### 39. leader / e  →  `grok/leader_e.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing side view facing right. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/e.png`  
รัน: `python tools/import_attack.py grok/leader_e.png leader e`

### 40. leader / se  →  `grok/leader_se.png`

```
Use the attached image as the exact character reference (same outfit, colors, proportions, weapon and chibi illustrated style). Draw a 4-frame attack animation strip of this character, frames side by side left to right, full body, same scale in every frame, feet on the same ground line, all frames facing three-quarter front view, turned to the viewer's right. Frame 1: winds the crescent-blade guandao (NOT a spear) back to one side. Frame 2: wide horizontal sweep. Frame 3: follow-through, golden cape flaring. Frame 4: back to the neutral standing pose. His weapon is a crescent-blade guandao, NOT a spear. Solid flat magenta background (#F3097A), no shadow, no ground, no text, wide empty gaps between frames so they never touch.
```

แนบ: `assets/dragon/leader.png` + `assets/dragon/facing/leader/se.png`  
รัน: `python tools/import_attack.py grok/leader_se.png leader se`
