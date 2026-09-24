import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for retro pixel icons and stars if not already present
css_to_add = '''
    /* Inline Retro Pixel Icons */
    .inline-pixel-icon {
      width: 14px;
      height: 14px;
      vertical-align: -2px;
      image-rendering: pixelated;
      image-rendering: -moz-crisp-edges;
      image-rendering: crisp-edges;
      display: inline-block;
      margin-right: 4px;
    }
    .bag-icon {
      width: 20px;
      height: 20px;
      vertical-align: -4px;
      margin-right: 7px;
      image-rendering: pixelated;
      image-rendering: -moz-crisp-edges;
      image-rendering: crisp-edges;
    }
    .webring-icon {
      width: 14px;
      height: 14px;
      vertical-align: -2px;
      image-rendering: pixelated;
      margin: 0 3px;
    }
    .rym-stars {
      display: inline-flex;
      gap: 2px;
      align-items: center;
      vertical-align: middle;
      margin-right: 4px;
    }
    .rym-star {
      width: 13px;
      height: 13px;
      image-rendering: pixelated;
    }
    .retro-alert-icon-img {
      width: 32px;
      height: 32px;
      image-rendering: pixelated;
      image-rendering: -moz-crisp-edges;
      image-rendering: crisp-edges;
    }
'''

if '.inline-pixel-icon' not in html:
    html = html.replace('/* CRT Scanlines Overlay */', css_to_add + '\n    /* CRT Scanlines Overlay */')

# 2. Replace Mood coffee emoji
html = html.replace(
    '<strong>SENTIMIENTO HOY:</strong> Desprecio acústico ☕<br>',
    '<strong>SENTIMIENTO HOY:</strong> Desprecio acústico <img src="assets/icons/coffee.svg" class="inline-pixel-icon" alt="Café"><br>'
)

# 3. Replace Live scrobble initial
html = html.replace(
    '<div class="lastfm-track" id="liveScrobble">\n                ♫ Slint — Washer (1991)\n              </div>',
    '<div class="lastfm-track" id="liveScrobble">\n                <img src="assets/icons/equalizer.svg" class="inline-pixel-icon" alt="Playing"> Slint — Washer (1991)\n              </div>'
)

# 4. Replace Action buttons
old_actions = '''            <!-- Quick Action Buttons with Custom Retro Alerts -->
            <div class="action-grid">
              <div class="btn-action" onclick="testCompatibility()">⚡ Test de Afinidad</div>
              <div class="btn-action" onclick="showRetroAlert('BANDEJA DE ENTRADA BLOQUEADA', 'Jaden: \\'Mi bandeja de entrada solo acepta ensayos de más de 1,000 palabras en formato PDF con análisis armónico sobre Steve Albini. Los correos sobre el pep rally son eliminados automáticamente.\\'', '✉')">✉ Enviar Ensayo</div>
              <div class="btn-action" onclick="showRetroAlert('ERROR 403: ACCESO DENEGADO', 'Jaden ha bloqueado permanentemente las solicitudes de amistad de toda persona que vista rojo universitario o aplauda en sincronía en el gimnasio.', '✖')">✖ Agregar a Amigos</div>
              <div class="btn-action" onclick="document.getElementById('secretVault').showModal()">🔒 Archivo Oculto</div>
            </div>'''

new_actions = '''            <!-- Quick Action Buttons with Custom Retro Alerts -->
            <div class="action-grid">
              <div class="btn-action" onclick="testCompatibility()"><img src="assets/icons/lightning.svg" class="inline-pixel-icon" alt="⚡"> Test de Afinidad</div>
              <div class="btn-action" onclick="showRetroAlert('BANDEJA DE ENTRADA BLOQUEADA', 'Jaden: \\'Mi bandeja de entrada solo acepta ensayos de más de 1,000 palabras en formato PDF con análisis armónico sobre Steve Albini. Los correos sobre el pep rally son eliminados automáticamente.\\'', 'mail')"><img src="assets/icons/mail.svg" class="inline-pixel-icon" alt="✉"> Enviar Ensayo</div>
              <div class="btn-action" onclick="showRetroAlert('ERROR 403: ACCESO DENEGADO', 'Jaden ha bloqueado permanentemente las solicitudes de amistad de toda persona que vista rojo universitario o aplauda en sincronía en el gimnasio.', 'error')"><img src="assets/icons/cross.svg" class="inline-pixel-icon" alt="✖"> Agregar a Amigos</div>
              <div class="btn-action" onclick="document.getElementById('secretVault').showModal()"><img src="assets/icons/lock.svg" class="inline-pixel-icon" alt="🔒"> Archivo Oculto</div>
            </div>'''

html = html.replace(old_actions, new_actions)

# 5. Replace Bag items (EDC)
old_bag = '''            <div class="bag-inspect-item" onclick="showRetroAlert('EQUIPO: AUDÍFONOS SONY MDR-7506', 'Audífonos con cable en espiral de 3 metros:\\nSu escudo acústico impenetrable para no escuchar los alaridos de Sharpay ni el rebote incesante de balones en el pasillo escolar.', '🎧')">
              🎧 <strong>Audífonos de Monitor de Estudio</strong>
            </div>
            <div class="bag-inspect-item" onclick="showRetroAlert('EQUIPO: IPOD CLASSIC 80GB', 'Con firmware alternativo Rockbox:\\nCero canciones de Disney. Contiene 4,200 pistas en FLAC 24-bit ripeadas directamente de sus vinilos a las 3:00 AM bajo la lluvia.', '📟')">
              📟 <strong>iPod Classic con Rueda de Clic</strong>
            </div>
            <div class="bag-inspect-item" onclick="showRetroAlert('HERRAMIENTA: SHARPIE NEGRO', 'Marcador permanente de punta biselada:\\nUtilizado para tachar rostros sonrientes en los afiches de audiciones y escribir comentarios cínicos en los casilleros del gimnasio.', '🖊')">
              🖊 <strong>Sharpie Negro Permanente</strong>
            </div>
            <div class="bag-inspect-item" onclick="showRetroAlert('SEGURIDAD: TAPONES DE SILICONA', 'Protección auditiva de grado industrial:\\nIndispensables cuando la Sra. Darbus realiza sus ejercicios de vocalización y ópera a las 8:00 AM en el vestíbulo.', '🔇')">
              🔇 <strong>Tapones de Cancelación de Ruido</strong>
            </div>'''

new_bag = '''            <div class="bag-inspect-item" onclick="showRetroAlert('EQUIPO: AUDÍFONOS SONY MDR-7506', 'Audífonos con cable en espiral de 3 metros:\\nSu escudo acústico impenetrable para no escuchar los alaridos de Sharpay ni el rebote incesante de balones en el pasillo escolar.', 'headphones')">
              <img src="assets/icons/headphones.svg" class="bag-icon" alt="Audífonos"> <strong>Audífonos de Monitor de Estudio</strong>
            </div>
            <div class="bag-inspect-item" onclick="showRetroAlert('EQUIPO: IPOD CLASSIC 80GB', 'Con firmware alternativo Rockbox:\\nCero canciones de Disney. Contiene 4,200 pistas en FLAC 24-bit ripeadas directamente de sus vinilos a las 3:00 AM bajo la lluvia.', 'ipod')">
              <img src="assets/icons/ipod.svg" class="bag-icon" alt="iPod"> <strong>iPod Classic con Rueda de Clic</strong>
            </div>
            <div class="bag-inspect-item" onclick="showRetroAlert('HERRAMIENTA: SHARPIE NEGRO', 'Marcador permanente de punta biselada:\\nUtilizado para tachar rostros sonrientes en los afiches de audiciones y escribir comentarios cínicos en los casilleros del gimnasio.', 'pen')">
              <img src="assets/icons/sharpie.svg" class="bag-icon" alt="Sharpie"> <strong>Sharpie Negro Permanente</strong>
            </div>
            <div class="bag-inspect-item" onclick="showRetroAlert('SEGURIDAD: TAPONES DE SILICONA', 'Protección auditiva de grado industrial:\\nIndispensables cuando la Sra. Darbus realiza sus ejercicios de vocalización y ópera a las 8:00 AM en el vestíbulo.', 'mute')">
              <img src="assets/icons/earplugs.svg" class="bag-icon" alt="Tapones"> <strong>Tapones de Cancelación de Ruido</strong>
            </div>'''

html = html.replace(old_bag, new_bag)

# 6. Replace Blinkies & Stamps symbols
old_blinkies = '''            <!-- Flashing Blinkies -->
            <div class="blinkies-container">
              <div class="blinkie b-wine">✖ EMO ONLINE ✖</div>
              <div class="blinkie b-green">● CASSETTE CULTURE ●</div>
              <div class="blinkie b-yellow">★ VINYL PURIST ★</div>
              <div class="blinkie b-wine">☠ NO POP RADIO ☠</div>
              <div class="blinkie b-green">► WINAMP POWERED ◄</div>
              <div class="blinkie b-yellow">✦ SLOWCORE ADDICT ✦</div>
            </div>'''

new_blinkies = '''            <!-- Flashing Blinkies -->
            <div class="blinkies-container">
              <div class="blinkie b-wine"><img src="assets/icons/cross.svg" class="inline-pixel-icon" style="width:10px;height:10px;margin:0 2px;"> EMO ONLINE <img src="assets/icons/cross.svg" class="inline-pixel-icon" style="width:10px;height:10px;margin:0 2px;"></div>
              <div class="blinkie b-green"><img src="assets/icons/cassette.svg" class="inline-pixel-icon" style="width:12px;height:12px;margin:0 2px;"> CASSETTE CULTURE <img src="assets/icons/cassette.svg" class="inline-pixel-icon" style="width:12px;height:12px;margin:0 2px;"></div>
              <div class="blinkie b-yellow"><img src="assets/icons/star_full.svg" class="inline-pixel-icon" style="width:10px;height:10px;margin:0 2px;"> VINYL PURIST <img src="assets/icons/star_full.svg" class="inline-pixel-icon" style="width:10px;height:10px;margin:0 2px;"></div>
              <div class="blinkie b-wine"><img src="assets/icons/skull.svg" class="inline-pixel-icon" style="width:11px;height:11px;margin:0 2px;"> NO POP RADIO <img src="assets/icons/skull.svg" class="inline-pixel-icon" style="width:11px;height:11px;margin:0 2px;"></div>
              <div class="blinkie b-green"><img src="assets/icons/equalizer.svg" class="inline-pixel-icon" style="width:11px;height:11px;margin:0 2px;"> WINAMP POWERED <img src="assets/icons/equalizer.svg" class="inline-pixel-icon" style="width:11px;height:11px;margin:0 2px;"></div>
              <div class="blinkie b-yellow"><img src="assets/icons/lightning.svg" class="inline-pixel-icon" style="width:10px;height:10px;margin:0 2px;"> SLOWCORE ADDICT <img src="assets/icons/lightning.svg" class="inline-pixel-icon" style="width:10px;height:10px;margin:0 2px;"></div>
            </div>'''

html = html.replace(old_blinkies, new_blinkies)

# Replace stamp text
html = html.replace('<div>♫ 180g<br>VINYL ONLY<br>NO MP3</div>', '<div><img src="assets/icons/equalizer.svg" style="width:13px;height:13px;display:block;margin:0 auto 2px;">180g<br>VINYL ONLY<br>NO MP3</div>')
html = html.replace('<div>☠ ANTI<br>BOLTON<br>WILDCATS</div>', '<div><img src="assets/icons/skull.svg" style="width:14px;height:14px;display:block;margin:0 auto 2px;">ANTI<br>BOLTON<br>WILDCATS</div>')
html = html.replace('<div>☕ COFFEE<br>&amp; SLINT<br>ALL NIGHT</div>', '<div><img src="assets/icons/coffee.svg" style="width:14px;height:14px;display:block;margin:0 auto 2px;">COFFEE<br>&amp; SLINT<br>ALL NIGHT</div>')
html = html.replace('<div>★ RYM TOP<br>REVIEWER<br>VERIFIED</div>', '<div><img src="assets/icons/star_full.svg" style="width:13px;height:13px;display:block;margin:0 auto 2px;">RYM TOP<br>REVIEWER<br>VERIFIED</div>')

# 7. Replace RateYourMusic Stars
html = html.replace(
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;">☆☆☆☆☆ [Bomba]</div>',
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;"><span class="rym-stars"><img src="assets/icons/star_half.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"></span> [Bomba]</div>'
)
html = html.replace(
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;">★☆☆☆☆ [Infrasónico]</div>',
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;"><span class="rym-stars"><img src="assets/icons/star_full.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"></span> [Infrasónico]</div>'
)
html = html.replace(
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;">★★½☆☆ [Mediocre]</div>',
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;"><span class="rym-stars"><img src="assets/icons/star_full.svg" class="rym-star"><img src="assets/icons/star_full.svg" class="rym-star"><img src="assets/icons/star_half.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"><img src="assets/icons/star_empty.svg" class="rym-star"></span> [Mediocre]</div>'
)
html = html.replace(
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;">★★★★½ [Magnum Opus]</div>',
    '<div style="color: var(--accent-rym-yellow); font-size: 9px;"><span class="rym-stars"><img src="assets/icons/star_full.svg" class="rym-star"><img src="assets/icons/star_full.svg" class="rym-star"><img src="assets/icons/star_full.svg" class="rym-star"><img src="assets/icons/star_full.svg" class="rym-star"><img src="assets/icons/star_half.svg" class="rym-star"></span> [Magnum Opus]</div>'
)

# 8. Replace Webring navigation
old_webring = '''          <div class="webring-nav">
            <a onclick="showRetroAlert('WEBRING // NAVEGACIÓN 2007', 'Conectando vía dial-up con el nodo anterior:\\n[xX_kurt_cobain_shrine_03_Xx] ... Servidor GeoCities en línea.', '🌐')">« Sitio Anterior</a>
            <a onclick="showRetroAlert('WEBRING // NAVEGACIÓN ALEATORIA', 'Redirigiendo a nodo aleatorio del anillo:\\n[slint-and-spiderland-fanpage.neocities.org] ... Conexión cifrada establecida.', '🎲')">[ ? ] Aleatorio</a>
            <a onclick="showRetroAlert('WEBRING // NAVEGACIÓN 2007', 'Conectando con el siguiente sitio del anillo:\\n[tape-recorder-hiss-society] ... Transmitiendo paquete de datos FLAC.', '🌐')">Sitio Siguiente »</a>
          </div>'''

new_webring = '''          <div class="webring-nav">
            <a onclick="showRetroAlert('WEBRING // NAVEGACIÓN 2007', 'Conectando vía dial-up con el nodo anterior:\\n[xX_kurt_cobain_shrine_03_Xx] ... Servidor GeoCities en línea.', 'globe')"><img src="assets/icons/globe.svg" class="webring-icon" alt="Globe"> « Sitio Anterior</a>
            <a onclick="showRetroAlert('WEBRING // NAVEGACIÓN ALEATORIA', 'Redirigiendo a nodo aleatorio del anillo:\\n[slint-and-spiderland-fanpage.neocities.org] ... Conexión cifrada establecida.', 'dice')"><img src="assets/icons/dice.svg" class="webring-icon" alt="Dice"> [ ? ] Aleatorio</a>
            <a onclick="showRetroAlert('WEBRING // NAVEGACIÓN 2007', 'Conectando con el siguiente sitio del anillo:\\n[tape-recorder-hiss-society] ... Transmitiendo paquete de datos FLAC.', 'globe')">Sitio Siguiente » <img src="assets/icons/globe.svg" class="webring-icon" alt="Globe"></a>
          </div>'''

html = html.replace(old_webring, new_webring)

# 9. Replace Secret Vault header
html = html.replace(
    '⚠ ARCHIVO CONFIDENCIAL // PARTICIÓN OCULTA WINDOWS XP',
    '<img src="assets/icons/warning.svg" class="inline-pixel-icon" style="width:16px;height:16px;vertical-align:-3px;" alt="!"> ARCHIVO CONFIDENCIAL // PARTICIÓN OCULTA WINDOWS XP'
)

# 10. Replace Retro Alert Modal HTML
old_modal = '''  <!-- ================= AUTHENTIC RETRO MODAL ALERT (WINDOWS XP / 2000s) ================= -->
  <dialog id="retroAlertModal" closedby="any">
    <div class="retro-alert-titlebar">
      <span id="retroAlertTitle">⚠ ALERTA DE SISTEMA // JADEN_OS</span>
      <span onclick="closeRetroAlert()" style="cursor:pointer; color:#fff; font-family:var(--font-mono); padding:0 3px;">✕</span>
    </div>
    <div class="retro-alert-body">
      <div class="retro-alert-icon-box" id="retroAlertIcon">⚠</div>
      <div class="retro-alert-text" id="retroAlertMsg">Contenido de la alerta...</div>
    </div>
    <div class="retro-alert-footer">
      <button class="retro-alert-btn" onclick="closeRetroAlert()">[ ACEPTAR ]</button>
    </div>
  </dialog>'''

new_modal = '''  <!-- ================= AUTHENTIC RETRO MODAL ALERT (WINDOWS XP / 2000s) ================= -->
  <dialog id="retroAlertModal" closedby="any">
    <div class="retro-alert-titlebar">
      <span id="retroAlertTitle"><img src="assets/icons/warning.svg" id="retroAlertTitleIcon" class="inline-pixel-icon" style="width:13px;height:13px;vertical-align:-2px;" alt="!"> ALERTA DE SISTEMA // JADEN_OS</span>
      <span onclick="closeRetroAlert()" style="cursor:pointer; color:#fff; font-family:var(--font-mono); padding:0 3px;">✕</span>
    </div>
    <div class="retro-alert-body">
      <div class="retro-alert-icon-box" id="retroAlertIcon">
        <img src="assets/icons/warning.svg" id="retroAlertIconImg" class="retro-alert-icon-img" alt="Icono de alerta">
      </div>
      <div class="retro-alert-text" id="retroAlertMsg">Contenido de la alerta...</div>
    </div>
    <div class="retro-alert-footer">
      <button class="retro-alert-btn" onclick="closeRetroAlert()">[ ACEPTAR ]</button>
    </div>
  </dialog>'''

html = html.replace(old_modal, new_modal)

# 11. Replace showRetroAlert implementation
old_func = '''    // Custom Retro Alert (Replaces browser alert)
    function showRetroAlert(title, message, icon = '⚠') {
      const modal = document.getElementById('retroAlertModal');
      document.getElementById('retroAlertTitle').textContent = `[!] ${title}`;
      document.getElementById('retroAlertMsg').textContent = message;
      document.getElementById('retroAlertIcon').textContent = icon;

      playAlertChime();
      modal.showModal();
    }'''

new_func = '''    const retroIconMap = {
      'warning': 'assets/icons/warning.svg',
      '⚠': 'assets/icons/warning.svg',
      'mail': 'assets/icons/mail.svg',
      '✉': 'assets/icons/mail.svg',
      'error': 'assets/icons/cross.svg',
      'cross': 'assets/icons/cross.svg',
      '✖': 'assets/icons/cross.svg',
      'lock': 'assets/icons/lock.svg',
      '🔒': 'assets/icons/lock.svg',
      'headphones': 'assets/icons/headphones.svg',
      '🎧': 'assets/icons/headphones.svg',
      'ipod': 'assets/icons/ipod.svg',
      '📟': 'assets/icons/ipod.svg',
      'pen': 'assets/icons/sharpie.svg',
      'sharpie': 'assets/icons/sharpie.svg',
      '🖊': 'assets/icons/sharpie.svg',
      'mute': 'assets/icons/earplugs.svg',
      'earplugs': 'assets/icons/earplugs.svg',
      '🔇': 'assets/icons/earplugs.svg',
      'globe': 'assets/icons/globe.svg',
      '🌐': 'assets/icons/globe.svg',
      'dice': 'assets/icons/dice.svg',
      '🎲': 'assets/icons/dice.svg',
      'lightning': 'assets/icons/lightning.svg',
      '⚡': 'assets/icons/lightning.svg',
      'coffee': 'assets/icons/coffee.svg',
      '☕': 'assets/icons/coffee.svg',
      'notepad': 'assets/icons/notepad.svg',
      '✍': 'assets/icons/notepad.svg',
      'skull': 'assets/icons/skull.svg',
      '☠': 'assets/icons/skull.svg',
      'cassette': 'assets/icons/cassette.svg'
    };

    // Custom Retro Alert (Replaces browser alert with authentic pixel icons)
    function showRetroAlert(title, message, iconType = 'warning') {
      const modal = document.getElementById('retroAlertModal');
      const iconPath = retroIconMap[iconType] || retroIconMap['warning'];

      document.getElementById('retroAlertTitle').innerHTML = `<img src="${iconPath}" class="inline-pixel-icon" style="width:13px;height:13px;vertical-align:-2px;" alt="!"> [!] ${title}`;
      document.getElementById('retroAlertMsg').textContent = message;

      const iconImg = document.getElementById('retroAlertIconImg');
      if (iconImg) {
        iconImg.src = iconPath;
        iconImg.alt = iconType;
      }

      playAlertChime();
      modal.showModal();
    }'''

html = html.replace(old_func, new_func)

# 12. Replace JS track change scrobble
html = html.replace(
    'document.getElementById(\'liveScrobble\').textContent = "♫ " + track.name;',
    'document.getElementById(\'liveScrobble\').innerHTML = \'<img src="assets/icons/equalizer.svg" class="inline-pixel-icon" alt="Playing"> \' + track.name;'
)

# 13. Replace testCompatibility icon call
html = html.replace(
    "showRetroAlert('RESULTADO: TEST DE AFINIDAD SÓNICA', results[Math.floor(Math.random() * results.length)], '⚡');",
    "showRetroAlert('RESULTADO: TEST DE AFINIDAD SÓNICA', results[Math.floor(Math.random() * results.length)], 'lightning');"
)

# 14. Replace submitComment icon call
html = html.replace(
    "showRetroAlert('LIBRO DE VISITAS // MENSAJE PUBLICADO', 'Tu comentario ha sido indexado en el registro de East High. Jaden ha emitido su réplica sarcástica.', '✍');",
    "showRetroAlert('LIBRO DE VISITAS // MENSAJE PUBLICADO', 'Tu comentario ha sido indexado en el registro de East High. Jaden ha emitido su réplica sarcástica.', 'notepad');"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html successfully!')
