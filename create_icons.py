import os

icons = {
    'warning.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Windows XP Style Warning Triangle -->
  <polygon points="16,2 31,28 1,28" fill="#ffcc00" stroke="#b38600" stroke-width="2" stroke-linejoin="round"/>
  <polygon points="16,5 29,26 3,26" fill="#ffe033"/>
  <!-- Exclamation Mark -->
  <rect x="14.5" y="10" width="3" height="9" rx="1.5" fill="#111"/>
  <circle cx="16" cy="22.5" r="1.8" fill="#111"/>
  <!-- Bevel highlights -->
  <line x1="16" y1="5" x2="3" y2="26" stroke="#fff" stroke-width="1.2" opacity="0.6"/>
</svg>''',

    'mail.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Windows XP / Outlook Envelope -->
  <rect x="2" y="7" width="28" height="19" rx="2" fill="#e8eaed" stroke="#546574" stroke-width="1.5"/>
  <!-- Envelope Flap & Backing -->
  <polygon points="2,7 16,19 30,7" fill="#d0d5dc" stroke="#546574" stroke-width="1.2"/>
  <polyline points="2,26 12,16" stroke="#a0aab5" stroke-width="1.2"/>
  <polyline points="30,26 20,16" stroke="#a0aab5" stroke-width="1.2"/>
  <!-- Folded Letter coming out -->
  <rect x="6" y="3" width="20" height="9" rx="1" fill="#ffffff" stroke="#334455" stroke-width="1"/>
  <line x1="9" y1="6" x2="19" y2="6" stroke="#891b38" stroke-width="1.2"/>
  <line x1="9" y1="9" x2="23" y2="9" stroke="#778899" stroke-width="1"/>
  <!-- Retro Red Postage Stamp -->
  <rect x="22" y="16" width="6" height="7" fill="#c41e3a" stroke="#fff" stroke-width="0.8"/>
  <circle cx="25" cy="19.5" r="1.5" fill="#fff" opacity="0.8"/>
</svg>''',

    'cross.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Windows XP Red Prohibited / Error Circle -->
  <circle cx="16" cy="16" r="14" fill="#cc1122" stroke="#800a15" stroke-width="2"/>
  <circle cx="16" cy="16" r="12" fill="#e61a2d"/>
  <circle cx="16" cy="14" r="10" fill="#ff3b4d" opacity="0.4"/>
  <!-- 3D White Cross -->
  <line x1="9" y1="9" x2="23" y2="23" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
  <line x1="23" y1="9" x2="9" y2="23" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
</svg>''',

    'lock.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Brass Padlock -->
  <!-- Silver Shackle -->
  <path d="M9,14 V9 A7,7 0 0,1 23,9 V14" fill="none" stroke="#b0b8c0" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M10,14 V9 A6,6 0 0,1 22,9 V14" fill="none" stroke="#e8eff5" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Brass Body -->
  <rect x="5" y="13" width="22" height="17" rx="3" fill="#d4af37" stroke="#8a7322" stroke-width="1.5"/>
  <rect x="7" y="15" width="18" height="13" rx="1.5" fill="#f5cd47"/>
  <!-- Keyhole -->
  <circle cx="16" cy="20" r="2.2" fill="#2b2005"/>
  <polygon points="15,20 17,20 17.5,25 14.5,25" fill="#2b2005"/>
</svg>''',

    'headphones.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Sony MDR-7506 Style Studio Headphones -->
  <!-- Headband -->
  <path d="M5,17 C5,8 10,4 16,4 C22,4 27,8 27,17" fill="none" stroke="#222" stroke-width="3" stroke-linecap="round"/>
  <path d="M7,14 C8,9 11,6 16,6 C21,6 24,9 25,14" fill="none" stroke="#555" stroke-width="1" stroke-linecap="round"/>
  <!-- Left Ear Cup -->
  <rect x="2" y="15" width="7" height="12" rx="3.5" fill="#1a1a1a" stroke="#444" stroke-width="1"/>
  <rect x="4" y="17" width="3" height="8" rx="1.5" fill="#0d0d0d"/>
  <rect x="2" y="19" width="3" height="4" fill="#0066cc" title="Left Blue Sticker"/>
  <!-- Right Ear Cup -->
  <rect x="23" y="15" width="7" height="12" rx="3.5" fill="#1a1a1a" stroke="#444" stroke-width="1"/>
  <rect x="25" y="17" width="3" height="8" rx="1.5" fill="#0d0d0d"/>
  <rect x="27" y="19" width="3" height="4" fill="#cc0022" title="Right Red Sticker"/>
  <!-- Coiled Cable -->
  <path d="M5.5,27 Q4,29 6,30 Q8,31 5,32" fill="none" stroke="#333" stroke-width="1.8"/>
</svg>''',

    'ipod.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Apple iPod Classic (Silver & Click Wheel) -->
  <rect x="6" y="2" width="20" height="28" rx="3" fill="#e3e5e8" stroke="#7a8288" stroke-width="1.5"/>
  <!-- Screen (Monochrome / Blue Backlit) -->
  <rect x="9" y="4" width="14" height="10" rx="1" fill="#759aa5" stroke="#334148" stroke-width="1"/>
  <!-- Screen Text Lines -->
  <line x1="11" y1="7" x2="19" y2="7" stroke="#1c2826" stroke-width="1"/>
  <line x1="11" y1="9" x2="21" y2="9" stroke="#1c2826" stroke-width="1"/>
  <line x1="11" y1="11" x2="16" y2="11" stroke="#1c2826" stroke-width="1"/>
  <!-- Click Wheel -->
  <circle cx="16" cy="22" r="6" fill="#f8f9fa" stroke="#b0b5ba" stroke-width="1"/>
  <circle cx="16" cy="22" r="2.2" fill="#d8dce0"/>
  <!-- Click Wheel MENU text hint -->
  <rect x="15" y="17" width="2" height="1" fill="#999"/>
</svg>''',

    'sharpie.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Black Sharpie Permanent Marker (Tilted) -->
  <g transform="rotate(-45 16 16)">
    <!-- Chisel Tip -->
    <polygon points="14,1 18,1 17,6 15,6" fill="#111111"/>
    <!-- Collar & Grip -->
    <rect x="14.5" y="6" width="3" height="3" fill="#silver" stroke="#999" stroke-width="0.5"/>
    <rect x="13.5" y="9" width="5" height="5" fill="#222"/>
    <!-- Main Body -->
    <rect x="13" y="14" width="6" height="16" rx="1" fill="#1c1c1c" stroke="#444" stroke-width="0.8"/>
    <!-- White Sharpie Logo streak -->
    <line x1="16" y1="17" x2="16" y2="24" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
    <!-- Cap top -->
    <rect x="13.5" y="30" width="5" height="2" rx="1" fill="#0a0a0a"/>
  </g>
</svg>''',

    'earplugs.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Industrial Foam Earplugs with Connecting Cord -->
  <!-- Blue Cord -->
  <path d="M8,18 C8,28 24,28 24,18" fill="none" stroke="#0077cc" stroke-width="1.8" stroke-dasharray="none"/>
  <!-- Left Yellow Plug -->
  <g transform="translate(4, 6) rotate(-15)">
    <polygon points="4,2 10,2 11,14 3,14" fill="#ffcc00" stroke="#cc9900" stroke-width="1"/>
    <ellipse cx="7" cy="2" rx="3" ry="1.5" fill="#ffee55"/>
    <line x1="4" y1="6" x2="10" y2="6" stroke="#cc9900" stroke-width="0.8"/>
    <line x1="3.5" y1="10" x2="10.5" y2="10" stroke="#cc9900" stroke-width="0.8"/>
  </g>
  <!-- Right Yellow Plug -->
  <g transform="translate(18, 5) rotate(15)">
    <polygon points="4,2 10,2 11,14 3,14" fill="#ffcc00" stroke="#cc9900" stroke-width="1"/>
    <ellipse cx="7" cy="2" rx="3" ry="1.5" fill="#ffee55"/>
    <line x1="4" y1="6" x2="10" y2="6" stroke="#cc9900" stroke-width="0.8"/>
    <line x1="3.5" y1="10" x2="10.5" y2="10" stroke="#cc9900" stroke-width="0.8"/>
  </g>
</svg>''',

    'globe.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Cyber / Webring Globe -->
  <circle cx="16" cy="16" r="13" fill="#003366" stroke="#5ef1f2" stroke-width="1.5"/>
  <!-- Grid Longitude lines -->
  <ellipse cx="16" cy="16" rx="6" ry="13" fill="none" stroke="#256d85" stroke-width="1"/>
  <line x1="3" y1="16" x2="29" y2="16" stroke="#256d85" stroke-width="1"/>
  <line x1="6" y1="10" x2="26" y2="10" stroke="#256d85" stroke-width="0.8"/>
  <line x1="6" y1="22" x2="26" y2="22" stroke="#256d85" stroke-width="0.8"/>
  <!-- Neon Green Continents Pixelated -->
  <path d="M12,7 Q15,6 18,9 Q19,13 15,14 Q13,12 12,7 Z" fill="#39ff14"/>
  <path d="M18,17 Q22,16 24,19 Q23,24 19,25 Q17,21 18,17 Z" fill="#39ff14"/>
  <path d="M7,13 Q10,14 9,18 Q7,19 6,15 Z" fill="#39ff14"/>
  <!-- Outer Glow Ring -->
  <circle cx="16" cy="16" r="14" fill="none" stroke="#5ef1f2" stroke-width="0.5" opacity="0.6"/>
</svg>''',

    'dice.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Emo Red / Black Casino Die -->
  <rect x="4" y="4" width="24" height="24" rx="5" fill="#891b38" stroke="#330814" stroke-width="2"/>
  <rect x="6" y="6" width="20" height="20" rx="3.5" fill="#a82245"/>
  <!-- White Pips (Number 5) -->
  <circle cx="10" cy="10" r="2.2" fill="#fff"/>
  <circle cx="22" cy="10" r="2.2" fill="#fff"/>
  <circle cx="16" cy="16" r="2.2" fill="#fff"/>
  <circle cx="10" cy="22" r="2.2" fill="#fff"/>
  <circle cx="22" cy="22" r="2.2" fill="#fff"/>
</svg>''',

    'lightning.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Electric Lightning Bolt -->
  <polygon points="18,1 7,17 15,17 12,31 25,13 17,13" fill="#ffea00" stroke="#b39b00" stroke-width="1.5" stroke-linejoin="round"/>
  <polygon points="17,3 9,16 15,16 13,27 23,14 17,14" fill="#ffffff" opacity="0.8"/>
</svg>''',

    'coffee.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Black Coffee Mug with Steam -->
  <!-- Steam curls -->
  <path d="M11,8 C10,5 12,3 11,1" fill="none" stroke="#888" stroke-width="1.2" stroke-linecap="round"/>
  <path d="M16,8 C15,4 18,3 16,1" fill="none" stroke="#bbb" stroke-width="1.2" stroke-linecap="round"/>
  <path d="M21,8 C20,5 22,3 21,1" fill="none" stroke="#888" stroke-width="1.2" stroke-linecap="round"/>
  <!-- Mug Body -->
  <rect x="6" y="9" width="16" height="18" rx="3" fill="#1b1d24" stroke="#4a5061" stroke-width="1.5"/>
  <!-- Mug Handle -->
  <path d="M22,12 C26,12 26,22 22,22" fill="none" stroke="#4a5061" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Dark Liquid Surface -->
  <ellipse cx="14" cy="10" rx="6.5" ry="2" fill="#3a1d0f"/>
</svg>''',

    'equalizer.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Winamp 2.91 Style Spectrum Equalizer Bars -->
  <rect x="2" y="2" width="28" height="28" rx="2" fill="#000000" stroke="#333333" stroke-width="1"/>
  <!-- Bar 1 -->
  <rect x="4" y="22" width="3.5" height="6" fill="#39ff14"/>
  <!-- Bar 2 -->
  <rect x="9.5" y="16" width="3.5" height="12" fill="#39ff14"/>
  <rect x="9.5" y="12" width="3.5" height="3" fill="#ffe033"/>
  <!-- Bar 3 -->
  <rect x="15" y="14" width="3.5" height="14" fill="#39ff14"/>
  <rect x="15" y="8" width="3.5" height="5" fill="#ffe033"/>
  <rect x="15" y="5" width="3.5" height="2" fill="#ff2244"/>
  <!-- Bar 4 -->
  <rect x="20.5" y="18" width="3.5" height="10" fill="#39ff14"/>
  <rect x="20.5" y="13" width="3.5" height="4" fill="#ffe033"/>
  <!-- Bar 5 -->
  <rect x="26" y="20" width="3.5" height="8" fill="#39ff14"/>
  <rect x="26" y="17" width="3.5" height="2" fill="#ffe033"/>
</svg>''',

    'notepad.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Windows XP Style Notepad Document with Pencil -->
  <!-- Notepad Paper -->
  <rect x="4" y="3" width="20" height="26" rx="1.5" fill="#ffffd9" stroke="#b0a875" stroke-width="1.2"/>
  <!-- Blue Ruled Lines -->
  <line x1="8" y1="8" x2="20" y2="8" stroke="#a0c0e0" stroke-width="1"/>
  <line x1="8" y1="12" x2="20" y2="12" stroke="#a0c0e0" stroke-width="1"/>
  <line x1="8" y1="16" x2="20" y2="16" stroke="#a0c0e0" stroke-width="1"/>
  <line x1="8" y1="20" x2="17" y2="20" stroke="#a0c0e0" stroke-width="1"/>
  <!-- Pencil -->
  <g transform="rotate(35 22 20)">
    <polygon points="18,10 22,10 20,6" fill="#f0d0b0"/>
    <polygon points="19.5,7 20.5,7 20,6" fill="#222"/>
    <rect x="18" y="10" width="4" height="15" fill="#ffcc00" stroke="#997700" stroke-width="0.5"/>
    <rect x="18" y="25" width="4" height="2" fill="#silver"/>
    <rect x="18" y="27" width="4" height="2.5" rx="1" fill="#ff6688"/>
  </g>
</svg>''',

    'star_full.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14">
  <!-- RateYourMusic Gold Star Full -->
  <polygon points="8,1 10.3,5.8 15.5,6.5 11.7,10.2 12.6,15.4 8,12.9 3.4,15.4 4.3,10.2 0.5,6.5 5.7,5.8" fill="#f8c025" stroke="#9e750a" stroke-width="0.8" stroke-linejoin="round"/>
</svg>''',

    'star_half.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14">
  <!-- RateYourMusic Gold Star Half -->
  <defs>
    <clipPath id="leftHalf">
      <rect x="0" y="0" width="8" height="16"/>
    </clipPath>
  </defs>
  <!-- Background empty star -->
  <polygon points="8,1 10.3,5.8 15.5,6.5 11.7,10.2 12.6,15.4 8,12.9 3.4,15.4 4.3,10.2 0.5,6.5 5.7,5.8" fill="#2a2820" stroke="#555" stroke-width="0.8" stroke-linejoin="round"/>
  <!-- Left half golden -->
  <polygon points="8,1 10.3,5.8 15.5,6.5 11.7,10.2 12.6,15.4 8,12.9 3.4,15.4 4.3,10.2 0.5,6.5 5.7,5.8" fill="#f8c025" stroke="#9e750a" stroke-width="0.8" stroke-linejoin="round" clip-path="url(#leftHalf)"/>
</svg>''',

    'star_empty.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="14" height="14">
  <!-- RateYourMusic Gold Star Empty -->
  <polygon points="8,1 10.3,5.8 15.5,6.5 11.7,10.2 12.6,15.4 8,12.9 3.4,15.4 4.3,10.2 0.5,6.5 5.7,5.8" fill="#22242a" stroke="#555866" stroke-width="0.8" stroke-linejoin="round"/>
</svg>''',

    'skull.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Emo Skull and Crossbones -->
  <line x1="4" y1="4" x2="28" y2="28" stroke="#891b38" stroke-width="4" stroke-linecap="round"/>
  <line x1="28" y1="4" x2="4" y2="28" stroke="#891b38" stroke-width="4" stroke-linecap="round"/>
  <path d="M8,14 C8,7 12,4 16,4 C20,4 24,7 24,14 C24,18 21,21 21,24 L11,24 C11,21 8,18 8,14 Z" fill="#e8eaed" stroke="#330814" stroke-width="1.5"/>
  <ellipse cx="12.5" cy="13.5" rx="2.5" ry="3" fill="#111"/>
  <ellipse cx="19.5" cy="13.5" rx="2.5" ry="3" fill="#111"/>
  <polygon points="16,17.5 15,19.5 17,19.5" fill="#111"/>
  <line x1="13" y1="22" x2="13" y2="24" stroke="#111" stroke-width="1"/>
  <line x1="16" y1="22" x2="16" y2="24" stroke="#111" stroke-width="1"/>
  <line x1="19" y1="22" x2="19" y2="24" stroke="#111" stroke-width="1"/>
</svg>''',

    'cassette.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <!-- Retro Analogue Cassette Tape -->
  <rect x="2" y="6" width="28" height="20" rx="3" fill="#1a1c22" stroke="#484f60" stroke-width="1.5"/>
  <polygon points="5,26 8,20 24,20 27,26" fill="#121317"/>
  <!-- Label Sticker -->
  <rect x="5" y="8" width="22" height="11" rx="1" fill="#e2e4e8" stroke="#8892a0" stroke-width="0.8"/>
  <line x1="7" y1="10" x2="25" y2="10" stroke="#891b38" stroke-width="1"/>
  <!-- Tape Spool Windows -->
  <rect x="9" y="11" width="14" height="6" rx="2" fill="#0d0e12"/>
  <circle cx="12" cy="14" r="2.2" fill="#fff" stroke="#555" stroke-width="0.5"/>
  <circle cx="20" cy="14" r="2.2" fill="#fff" stroke="#555" stroke-width="0.5"/>
  <line x1="12" y1="14" x2="20" y2="14" stroke="#683e20" stroke-width="2"/>
</svg>'''
}

dest_dir = os.path.join('assets', 'icons')
os.makedirs(dest_dir, exist_ok=True)

for filename, content in icons.items():
    filepath = os.path.join(dest_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Generated {filepath}")
