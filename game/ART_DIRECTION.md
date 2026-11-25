# ECHOES OF THE GRID
## Art Direction & Asset Production Standards

**Version:** 1.0  
**Engine:** Godot  
**Art Style:** Stardew Valley-inspired 2D Pixel Art  
**Genre:** Science Fiction, Exploration, Mystery, Atmospheric Horror  
**Document Status:** Approved Art Direction

---

# 1. Art Direction Overview

## 1.1 Visual Identity

ECHOES OF THE GRID is a 2D pixel-art science-fiction adventure game inspired by the visual readability, environmental detail, and cohesive art style of Stardew Valley.

Unlike Stardew Valley's colorful rural setting, ECHOES OF THE GRID takes place inside a damaged futuristic space station featuring abandoned laboratories, industrial facilities, defensive robots, and mysterious extraterrestrial creatures.

The game's visual identity combines:

- Detailed, readable pixel art.
- Futuristic industrial architecture.
- Abandoned and damaged space-station environments.
- Warm technological lighting contrasted with cold surroundings.
- Eerie silhouettes and atmospheric psychological horror.
- Environmental storytelling through lighting, objects, and damage.

The overall atmosphere should communicate isolation, mystery, technological advancement, and the presence of an unknown threat.

## 1.2 Core Art Principles

All visual assets must follow these principles:

1. **Consistency:** Characters, environments, props, and interfaces must share a coherent pixel-art style.
2. **Readability:** Important characters, objects, and interactable elements must remain recognizable at normal gameplay scale.
3. **Atmosphere:** Lighting, colors, and environmental details must reinforce the game's science-fiction mystery and horror elements.
4. **Functionality:** Asset designs should visually communicate their gameplay purpose.
5. **Originality:** Stardew Valley serves as inspiration for pixel-art presentation, not as a source for copying existing assets.
6. **Performance:** Assets must remain suitable for a 2D Godot game.

---

# 2. Visual Style

## 2.1 Rendering Style

The game uses detailed, stylized 2D pixel art.

Visual characteristics include:

- Clearly defined pixel clusters.
- Recognizable character and object silhouettes.
- Controlled color palettes.
- Intentional shading and highlights.
- Consistent outlines or dark edge treatments.
- Consistent pixel density across production assets.
- Minimal use of gradients and anti-aliasing.

Avoid:

- Mixing unrelated art styles.
- Using photorealistic textures as production sprites.
- Inconsistent pixel sizes.
- Excessive anti-aliasing.
- Unnecessarily detailed sprites that become unreadable.
- Inconsistent character proportions.

Detailed concept illustrations are permitted as design references, but all in-game character and environment assets must follow the approved pixel-art style.

## 2.2 Camera Perspective

The game uses a **Stardew Valley-inspired top-down 2D perspective**, with angled views of characters, walls, and environmental objects.

This perspective allows players to observe the floor, surrounding environments, characters, machinery, and interactable objects.

All environment and character assets must follow a consistent perspective.

## 2.3 Visual Detail Level

The game uses medium-detail pixel art.

Characters should have sufficient detail to communicate their identities, while environments may include additional decorative elements to establish atmosphere and environmental storytelling.

Important gameplay objects must remain visually distinguishable from decorative elements.

---

# 3. Resolution and Pixel Standards

## 3.1 Base Game Resolution

- **Internal resolution:** 640 × 360 pixels.
- **Aspect ratio:** 16:9.
- **Rendering:** Pixel-perfect-oriented 2D rendering.
- **Scaling:** Prefer integer scaling where supported.
- **Texture filtering:** Nearest-neighbor for pixel-art assets.

The game must preserve sharp pixel edges when displayed at larger resolutions.

Godot viewport and stretch settings must be configured to minimize distortion and uneven pixel scaling.

## 3.2 Tile Size

The standard environment tile size is:

**16 × 16 pixels**

This grid applies to:

- Floors.
- Walls.
- Corridors.
- Laboratory surfaces.
- Storage areas.
- Environmental decorations.

Larger structures may occupy multiple tiles.

Examples:

| Asset | Dimensions |
|---|---|
| Standard floor tile | 16 × 16 px |
| Large floor pattern | 32 × 32 px |
| Medium environmental prop | 32 × 32 px |
| Large environmental prop | 64 × 64 px |
| Large machinery | Multiple tiles |

The tile size defines the environment grid, not the maximum size of individual objects.

## 3.3 Character Sprite Dimensions

The following dimensions define the standard animation-frame canvases.

| Character | Frame canvas |
|---|---|
| Void Runner | 32 × 48 px |
| ECH0 | 32 × 32 px |
| VanGrid | 48 × 48 px |
| Void Born | 64 × 80 px |

These dimensions include transparent space needed for character movement and animation.

The visible character does not need to occupy the entire canvas.

All characters must maintain consistent world proportions and pixel density.

## 3.4 Object and UI Dimensions

| Asset type | Standard dimensions |
|---|---|
| Small item | 16 × 16 px |
| Medium prop | 32 × 32 px |
| Large prop | 48 × 48 or 64 × 64 px |
| Small UI icon | 16 × 16 px |
| Standard UI icon | 32 × 32 px |
| Environment tile | 16 × 16 px |
| Large machinery | Variable, grid-aligned |

Asset dimensions may increase when necessary to accommodate larger structures or animations.

## 3.5 Pixel Density and Scaling

All production sprites must maintain consistent pixel density.

Characters and objects appearing at the same world scale should use similarly sized visual pixels.

Avoid arbitrary non-integer scaling of pixel-art assets.

Nearest-neighbor filtering must be used for pixel-art textures to preserve sharp edges.

---

# 4. Character Art Direction

## 4.1 Void Runner — Player Character

The Void Runner is a trained space explorer deployed by ATLAS.

### Design Characteristics

- Futuristic exploration suit.
- Recognizable helmet and body silhouette.
- Protective equipment.
- Industrial design consistent with ATLAS technology.
- Compact proportions appropriate for pixel art.

The Void Runner must remain visible against dark station environments.

### Required Directions

- Front / Down.
- Back / Up.
- Left.
- Right.

### Core Animations

- Idle.
- Walking.
- Interacting.
- Inspecting equipment.

Additional animations may be introduced as gameplay requires.

## 4.2 ECH0 — AI Companion

ECH0 is the player's friendly hovering AI companion.

The approved ECH0 concept sheet serves as the official character design reference.

### Established Appearance

- White rounded body.
- Black expressive face display.
- Warm amber lighting.
- Compact hovering design.
- Small articulated arms.
- Friendly silhouette.

### Pixel-Art Adaptation

ECH0's pixel-art design must preserve its established visual identity.

The following features are essential:

- Expressive digital eyes.
- Rounded white body.
- Amber lighting.
- Hovering movement.
- Recognizable face display.

### Core Animations

- Idle hover.
- Following the player.
- Speaking.
- Thinking.
- Alert.
- Happy.
- Concerned.

ECH0 should remain visually approachable and contrast with the threatening Void Born.

## 4.3 VanGrid — ATLAS Defense Robot

VanGrids are industrial defense and utility robots deployed throughout the GRID.

The latest approved compact tracked VanGrid concept sheet serves as the official design reference.

### Established Appearance

- Predominantly white industrial armor.
- Compact tracked chassis.
- Mechanical arms or manipulators.
- Amber sensors.
- ATLAS branding.
- Durable industrial construction.

### Design Requirements

VanGrids must appear functional, mechanical, and capable of performing physical tasks.

They must remain visually distinct from ECH0.

VanGrids must not use ECH0's floating companion design.

### Modular Components

The design supports identifiable components, including:

- Head or sensor assembly.
- Main chassis.
- Mechanical arms.
- Power core.
- Mobility components.

### Core Animations

- Idle.
- Moving.
- Scanning.
- Interacting with equipment.
- Deploying.
- Defending.
- Damaged or disabled.

ATLAS branding should be visible when sprite dimensions allow. Small sprites may use a simplified ATLAS insignia.

## 4.4 Void Born — Alien Threat

Void Born are mysterious extraterrestrial creatures associated with the destruction of the GRID.

The approved void-black creature concept serves as the official design reference.

### Established Appearance

- Tall, elongated humanoid anatomy.
- Unnaturally long limbs.
- Clawed hands.
- Narrow torso.
- Predatory posture.
- Tail.
- Void-black body.
- Subtle violet highlights.

### Design Requirements

Void Born must appear unsettling, mysterious, and visually distinct from ATLAS technology.

Their silhouettes must remain recognizable in dim environments.

Void black must dominate their appearance.

Violet highlights should be restrained and used to emphasize selected anatomical details or unnatural features.

### Horror Presentation

Void Born may appear:

- Standing motionless in distant corridors.
- Partially obscured by machinery.
- Watching through observation windows.
- Moving across dark areas.
- Appearing in damaged security footage.

### Core Animations

- Idle stalking.
- Walking.
- Running.
- Turning.
- Threatening posture.

Additional animations may be implemented according to gameplay requirements.

---

# 5. Color Palette

## 5.1 ATLAS and GRID Palette

| Purpose | Color | Hex |
|---|---|---|
| Primary background | Dark Navy | `#111827` |
| Metallic surfaces | Steel Gray | `#475569` |
| Machinery and panels | Gunmetal | `#374151` |
| ATLAS armor | Off-White | `#E5E7EB` |
| Active technology | Amber | `#F59E0B` |
| Secondary technology | Cyan | `#22D3EE` |
| Emergency and danger | Red | `#DC2626` |

These colors serve as base references. Shading may use appropriate lighter and darker variations.

## 5.2 Void Born Palette

| Purpose | Color | Hex |
|---|---|---|
| Primary body | Void Black | `#0B0812` |
| Secondary body | Dark Violet | `#21162F` |
| Subtle highlights | Muted Purple | `#563578` |
| Bioluminescence | Pale Violet | `#A78BFA` |

Violet should be used sparingly to preserve the Void Born's eerie appearance.

## 5.3 Color Usage Rules

- Amber identifies active ATLAS technology.
- Cool blue-gray tones dominate station environments.
- Red indicates danger, warnings, or emergencies.
- Violet is associated with Void Born activity.
- Excessive saturation should be avoided.
- Important gameplay elements must maintain sufficient contrast.

---

# 6. Environment Art Direction

## 6.1 GRID Architecture

The GRID is a large industrial research and defense station.

Its environments share a consistent architectural language.

Common visual elements include:

- Metallic walls and floors.
- Modular corridors.
- Industrial doors.
- Pipes and ventilation systems.
- Control terminals.
- Warning signs.
- Damaged electrical equipment.
- Emergency lighting.
- Storage containers.
- Laboratory machinery.

## 6.2 Storage Facility

The Storage Facility should feel organized, industrial, and functional.

Its visual elements include:

- Component receiving areas.
- Equipment scanners.
- Storage racks.
- Classification terminals.
- Component testing chambers.
- VanGrid production machinery.

The environment should communicate inspection, classification, and equipment restoration.

## 6.3 Research Facility

The Research Facility should feel scientific, mysterious, and unsettling.

Its visual elements include:

- Specimen containment chambers.
- Research terminals.
- Observation windows.
- Laboratory equipment.
- Damaged research records.
- Experimental machinery.
- Simulation chambers.

Research areas should use colder lighting and stronger environmental storytelling.

## 6.4 Corridors and Exploration Areas

Corridors connect the GRID's facilities.

They should include:

- Consistent architectural elements.
- Distinctive signage.
- Environmental landmarks.
- Visible structural damage.
- Lighting differences between operational and abandoned sections.
- Occasional environmental hazards.

Each section must remain visually distinguishable while belonging to the same station.

---

# 7. Lighting and Horror Atmosphere

## 7.1 Lighting Style

The game uses hybrid pixel-art lighting.

This combines:

- Hand-authored sprite shading.
- Environmental lighting.
- Controlled Godot 2D lighting.
- Emergency lighting effects.

Lighting must preserve pixel-art readability.

## 7.2 Horror Direction

The game emphasizes atmospheric suspense and uncertainty rather than constant jumpscares.

Horror elements may include:

- Flickering lights.
- Distant silhouettes.
- Moving shadows.
- Security-camera sightings.
- Sudden environmental sounds.
- Unexplained movement.
- Occasional scripted Void Born encounters.

Horror sequences should support exploration and storytelling without unnecessarily interrupting educational activities.

## 7.3 Visibility

Dark environments must preserve the visibility of:

- The player.
- Important interactable objects.
- Navigation landmarks.
- Critical gameplay information.

Void Born may be intentionally difficult to see, but navigation and essential interactions must remain readable.

---

# 8. Sprite Orientation and Animation

## 8.1 Directional Standards

Characters use four-directional sprites:

1. Front / Down.
2. Back / Up.
3. Left.
4. Right.

Horizontal mirroring may be used when appropriate, provided it does not create incorrect asymmetrical details or reversed branding.

## 8.2 Animation Frame Rates

| Animation | Standard playback |
|---|---|
| Idle | 4–6 FPS |
| Walking | 8 FPS |
| Running | 10–12 FPS |
| Interacting | 6–8 FPS |
| Mechanical actions | Based on action |
| Horror sequences | Based on intended effect |

Animation timing should prioritize readable and natural movement.

## 8.3 Sprite Sheet Standards

Sprite sheets must use:

- Consistent frame dimensions.
- Clearly defined animation sequences.
- Predictable frame ordering.
- Transparent backgrounds.
- Stable character alignment.
- No unnecessary spacing unless documented.

Animation frames must not introduce unintended position shifts.

---

# 9. UI and Holographic Interfaces

## 9.1 UI Visual Style

The interface should resemble the technology available inside the GRID.

Examples include:

- Holographic Object Profiles.
- Component inspection displays.
- Research archives.
- Diagnostic results.
- ECH0 dialogue panels.
- Mission information.

## 9.2 UI Principles

- Maintain readable text.
- Use consistent icons.
- Preserve clear visual hierarchy.
- Avoid excessive decorative effects.
- Keep important information distinguishable from the background.

## 9.3 UI Scaling

UI elements may use higher-resolution rendering when necessary to preserve text readability.

UI scaling must be tested independently from world-sprite scaling.

Interfaces must remain readable at common desktop display resolutions.

---

# 10. Asset Export and Godot Standards

## 10.1 File Formats

| Asset type | Format |
|---|---|
| Character sprites | PNG |
| Sprite sheets | PNG |
| Environment tiles | PNG |
| UI icons | PNG or SVG |
| Concept references | PNG |
| Sound effects | WAV or OGG |
| Music | OGG |

Transparent backgrounds must be used where applicable.

## 10.2 Naming Conventions

Use descriptive lowercase filenames with underscores.

Examples:

- `ech0_idle_down.png`
- `vangrid_walk_left.png`
- `voidborn_stalk_right.png`
- `grid_floor_metal_01.png`
- `atlas_terminal_active.png`

Naming conventions must remain consistent with `CONTRIBUTING.md`.

## 10.3 Godot Import Standards

- Use nearest-neighbor filtering for pixel-art textures.
- Avoid unintended texture smoothing.
- Preserve consistent sprite scales.
- Configure appropriate viewport scaling.
- Verify animation frame boundaries.
- Verify sprite alignment.
- Test assets inside their intended Godot scenes.

---

# 11. AI-Generated Asset Standards

AI-generated assets must follow the approved art direction and character references.

Before generating an asset:

1. Identify the intended asset category.
2. Consult the approved visual references.
3. Follow the established pixel-art style.
4. Apply the correct color palette.
5. Follow the specified dimensions and orientation.
6. Preserve established character designs.

Before accepting an asset:

1. Verify visual consistency.
2. Check dimensions.
3. Check orientation.
4. Check transparency.
5. Inspect pixel-art quality.
6. Verify world-scale consistency.
7. Test the asset in Godot.

AI-generated images may require cleanup, resizing, alignment, or manual pixel-art adjustments before becoming production-ready.

Generated assets must not automatically replace approved designs.

---

# 12. Reference Asset Management

Approved references are stored under:

`assets/references/`

Recommended organization:

```text
assets/references/
├── art-style/
├── ech0/
├── vangrid/
├── voidborn/
├── characters/
├── environments/
└── ui/
```

Approved concept sheets define character identity.

Production sprites must preserve those identities while following the game's pixel-art standards.

The approved reference library is the primary visual guide for future asset generation.

---

# 13. Asset Approval Workflow

All new assets follow the same process.

### Step 1 — Concept Design

Establish the intended appearance using the art direction and approved references.

### Step 2 — Pixel-Art Adaptation

Translate the approved design into the established rendering style, proportions, and dimensions.

### Step 3 — Technical Validation

Verify dimensions, transparency, orientation, alignment, and animation requirements.

### Step 4 — In-Game Testing

Import the asset into Godot and evaluate its appearance at the intended gameplay resolution.

### Step 5 — Team Approval

Accept, revise, or reject the asset.

Only approved assets become official production references.

---

# 14. Final Art Direction Statement

ECHOES OF THE GRID combines the readability and charm of Stardew Valley-inspired pixel art with the atmosphere of a mysterious, abandoned science-fiction research station.

Its characters, environments, props, and interfaces must form a cohesive visual world.

ECH0 represents friendly and approachable technology.

VanGrids represent functional ATLAS defense machinery.

Void Born represent the unknown and unsettling dangers beyond humanity's understanding.

The game balances visual clarity, environmental storytelling, and atmospheric horror while supporting exploration and educational gameplay.

All future assets must follow this document and the approved visual references.

**Document Version: 1.0 — Approved Art Direction**
