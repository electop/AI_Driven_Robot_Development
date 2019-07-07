# Cura Print settings
   ## Prerequites
   - Cura 4.1.0
   - CR-10S5 or ANET A8(Prusa i3)
   - OctoPrint 1.3.11
   ## Settings
   ```
   This setting is based on my experience.
   If you have nice recommendations better than me, please let me know.
   For reference, if necessary, I will update continuously.
   ```
   ### Quality
   - Layer Height : 0.2mm
   - initial Layer Height : 0.26mm
   - Line Width : 0.4mm
       - Wall Line Width : 0.4mm
           - Outer Wall Line Width : 0.4mm
           - Inner Wall(s) Line Width : 0.4mm
       - Top/Bottom Line Width : 0.4mm
       - Infill Line Width : 0.4mm
       - Initial Layer Line Width : 100%
   ### Shell
   - Wall Thickness : 0.8mm
       - Wall Line Count : 2
   - Top/Bottom Thickness : 0.8mm
       - Top Thickness : 0.8mm
           - Top Layers : 4
       - Bottom Thickness : 0.8mm
           - Bottom Layers : 4
   - Top/Bottom Pattern : Concentric
       ```
       Lines, zig zag, concentric and 'line direction' with custom value [90]
       ```
       <img src="https://ultimaker.com/photo/image/1300x0/5a71dfed3bb56/TopBottomPattern.png">
   - Optimize Wall Printing Order : check
   - Fill Gaps Between Walls : Everywhere
       <img src="https://ultimaker.com/photo/image/1300x0/592c1cd715c45/Fill-gaps-between-walls.png" width="480"><br>
   - Horizontal Expansion : 0mm
   - Enable Ironing : check
   ### Infill
   - Infill Density : 15%
       - Infill Line Distance : 8.0mm
   - Infill Pattern : <a href="https://ultimaker.com/en/resources/52670-infill">Cubic Subdivision</a>
     ```
     Grid: Strong 2D infill
     Lines: Quick 2D infill
     Triangles: Strong 2D infill
     Tri-hexagon: Strong 2D infill
     Cubic: Strong 3D infill
     Cubic (subdivision): Strong 3D infill (this saves material compared to Cubic)
     Octet: Strong 3D infill
     Quarter cubic: Strong 3D infill
     Concentric: Flexible 3D infill
     Concentric 3D : Flexible 3D infill
     Zig-zag: A grid shaped infill, printing continuously in one diagonal direction
     Cross: Flexible 3D infill
     Cross 3D: Flexible 3D infill
     ```
     <img src="https://ultimaker.com/photo/image/1300x0/5b33789c313a7/InfillPatterns.png" title="">
   - Infill Line Multiplier : 1
   - Infill Overlap Percentage : 10%
     <img src="https://ultimaker.com/photo/image/1300x0/5b3378e4b3201/Infill-overlap-NEW.png" width="320" title=""><br>
   - Infill Layer Thickness : 0.2mm
   - Infill Before Walls : no check
   ### Material
   - Printing Temperature : 185℃
   - Printing Temperature Initial Layer : 185℃
   - Initial Printing Temperature : 175℃
   - Final Printing Temperature : 170℃
   - Build Plate Temperature : 20℃
   - Build Plate Temperature Initial Layer : 20℃
   - Enable Retraction : check
   - Retract at Layer Change : check
   - Retraction Distance : 10
   - Retraction Speed : 100mm/s
   ### Speed
   - Print Speed : 50mm/s
       - Infill Speed : 30mm/s
       - Wall Speed : 25.0mm/s
           - Outer Wall Speed : 30mm/s
           - Inner Wall Speed : 50mm/s
       - Top/Bottom Speed : 20m/s
       - Support Speed : 40mm/s
           - Support Infill Speed : 50mm/s
           - Support Interface Speed : 26.6667mm/s
               - Support Floor Speed : 30mm/s
   - Travel Speed : 100mm/s
   - Initial Layer Speed : 25.0mm/s
       - Initial Layer Print Speed : 20mm/s
       - Initial Layer Travel Speed : 30mm/s
   - Skirt/Brim Speed : 30mm/s
   - Maximum Z Speed : 100mm/s
   - Enable Acceleration Control : no check
   - Enable Jerk Control : no check
   ### Travel
   - Combining Mode : Off
   - Avoid Printed Parts When Traveling : check
   - Z Hop When Retracted : check
   - Z Hop Only Over Printed Parts : no check
   - Z Hop Height : 0.5mm
   ### Cooling
   - Enable Print Cooling : check
   - Fan Speed : 100.0%
      - Regular Fan Speed : 100.0%
      - Maximum Fan Speed : 100.0%
   - Regular/Maximum Speed Threshold : 10s
   - Initial Fan Speed : 0%
   - Regular Fan Speed at Height : 0.32mm
       - Regular Fan Speed at Layer : 2
   - Minimum Layer Time : 0
   - Minimum Speed : 10mm/s
   - Lift Head : no check
   ### Support
   - Generate Support : check
   - Support Placement : Everywhere
   - Support Overhang Angle : 50
   - Support Pattern : <a href="https://ultimaker.com/en/resources/20422-cura-support-settings">Triangles</a>
     <img src="https://ultimaker.com/photo/image/1300x0/5744447ebb127/Support-patterns.png">
   - Support Density : 15%
   - Support Horizontal Expansion : 0mm
   - Support Infil Layer Thickness : 0.2mm
   - Gradual Support Infill Steps : 0
   - Enable Support Interface : check
       - Enable Support Roof : check
       - Enable Support Floor : check
   ### Build Plate Adhesion
   - Build Plate Adhesion Type : Brim
   - Brim Width : 6mm
       - Brim Line Count : 15
   - Brim Only on Outside : no check
   ### Dual Extrusion : No item
   ### Special Modes
   - Print Sequence : All at Once
   - Surface Mode : Normal
   - Spiralize Outer Contour : no check
   ### Experimental : No item
   
