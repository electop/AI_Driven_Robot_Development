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
   - initial Layer Height : 0.25mm
   - Line Width : 0.4mm
       - Wall Line Width : 0.4mm
           - Outer Wall Line Width : 0.4mm
           - Inner Wall(s) Line Width : 0.4mm
       - Top/Bottom Line Width : 0.4mm
       - Infill Line Width : 0.4mm
       - Initial Layer Line Width : 100%
   ### Shell
   - Wall Thickness : 1.2mm
       - Wall Line Count : 3
   - Top/Bottom Thickness : 1.2mm
       - Top Thickness : 1.2mm
           - Top Layers : 6
       - Bottom Thickness : 1.2mm
           - Bottom Layers : 6
   - Optimize Wall Printing Order : no check
   - Fill Gaps Between Walls : Everywhere
   - Horizontal Expansion : 0mm
   - Enable Ironing : 0mm
   ### Infill
   - Infill Density : 40%
       - Infill Line Distance : 3.0mm
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
   - Infill Layer Thickness : 0.2mm
   - Infill Before Walls : no check
   ### Material
   - Printing Temperature : 200
   - Printing Temperature Initial Layer : 200
   - Initial Printing Temperature : 190
   - Final Printing Temperature : 185
   - Build Plate Temperature : 20
   - Build Plate Temperature Initial Layer : 20
   - Enable Retraction : check
   - Retract at Layer Change : no check
   - Retraction Distance : 1.7
   - Retraction Speed : 45mm/s
   ### Speed
   - Print Speed : 40mm/s
       - Infill Speed : 40mm/s
       - Wall Speed : 20.0mm/s
           - Outer Wall Speed : 20mm/s
           - Inner Wall Speed : 40mm/s
       - Top/Bottom Speed : 20m/s
       - Support Speed : 40mm/s
           - Support Floor Speed : 20mm/s
   - Travel Speed : 60mm/s
   - Initial Layer Speed : 20.0mm/s
       - Initial Layer Print Speed : 10mm/s
       - Initial Layer Travel Speed : 10mm/s
   - Skirt/Brim Speed : 10mm/s
   - Maximum Z Speed : 40mm/s
   - Enable Acceleration Control : no check
   - Enable Jerk Control : no check
   ### Travel
   - Combining Mode : Not in Skin
   - Avoid Printed Parts When Traveling : check
   - Avoid Supports When Traveling : no check
   - Travel Avoid Distance : 0.625mm
   - Z Hop When Retracted : check
   - Z Hop Only Over Printed Parts : no check
   - Z Hop Height : 1mm
   ### Cooling
   - Enable Print Cooling : check
   - Fan Speed : 100.0%
      - Regular Fan Speed : 100.0%
      - Maximum Fan Speed : 100.0%
   - Regular/Maximum Speed Threshold : 10s
   - Initial Fan Speed : 0%
   - Regular Fan Speed at Height : 0.25mm
       - Regular Fan Speed at Layer : 2
   - Minimum Layer Time : 0
   - Minimum Speed : 10mm/s
   - Lift Head : no check
   ### Support
   - Generate Support : check
   - Support Placement : Everywhere
   - Support Overhang Angle : 55
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
   - Build Plate Adhesion Type : Skirt
   - Skirt Line Count : 6
   ### Dual Extrusion : No item
   ### Special Modes
   - Print Sequence : All at Once
   - Surface Mode : Normal
   - Spiralize Outer Contour : no check
   ### Experimental : No item
   
