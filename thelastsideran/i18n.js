(function () {
  function detectLang() {
    var q = '';
    try { q = new URLSearchParams(location.search).get('lang') || ''; } catch (e) {}
    q = String(q).toLowerCase();
    if (q.indexOf('ja') === 0) return 'ja';
    if (q.indexOf('es') === 0) return 'es';
    if (q.indexOf('en') === 0) return 'en';

    var langs = navigator.languages && navigator.languages.length
      ? navigator.languages
      : [navigator.language || 'en'];
    var primary = String(langs[0] || navigator.language || 'en').toLowerCase();
    if (primary.indexOf('ja') === 0) return 'ja';

    function has(prefix) {
      for (var i = 0; i < langs.length; i++) {
        if (String(langs[i]).toLowerCase().indexOf(prefix) === 0) return true;
      }
      return false;
    }
    if (has('es')) return 'es';
    return 'en';
  }

  var STRINGS = {
    ja: {
      pageTitle: 'ザ・ラスト・サイデラン',
      metaDescription: 'ザ・ラスト・サイデラン — PixelDo Gamesのスピーディーなアーケード宇宙シューティング。ゼニアを操り、スパイクAIと戦い、星のエッセンスを集めて機体とストーリーを解放し、ボスを生き残れ。Steamで配信中。itch.ioで無料デモ公開。iOS / Android近日公開。',
      ogTitle: 'ザ・ラスト・サイデラン',
      ogDescription: 'ゼニアを操れ。スパイクと戦え。機体とストーリーを解放せよ。Steamで配信中。itch.ioで無料デモ公開。iOS / Android近日公開。',
      taglineHtml: 'スパイクと戦え。<br> 機体とストーリーを解放。生き残れ。',
      launchSteam: 'Steamで配信中',
      launchItch: 'itch.ioで無料デモ',
      launchMobile: 'iOS / Android近日公開',
      badgeItchPrefix: '無料デモで遊ぶ',
      badgeItchAria: 'itch.ioで『ザ・ラスト・サイデラン』の無料デモをプレイ',
      badgeSteamPrefix: '今すぐ入手',
      badgeSteamAria: 'Steamで『ザ・ラスト・サイデラン』を入手',
      badgeIosPrefix: 'ダウンロード',
      badgeIosAria: 'App Store — 近日公開',
      badgeAndroidPrefix: '今すぐ入手',
      badgeAndroidAria: 'Google Play — 近日公開',
      heroNote: 'フルゲームはSteamで配信中。無料デモはitch.ioで。iOS / Androidは近日公開。',
      trailerHeading: 'トレーラー',
      trailerLabel: '公式トレーラーを見る',
      trailerAria: '公式トレーラーを再生',
      trailerIframeTitle: 'ザ・ラスト・サイデラン トレーラー',
      ctaHeading: 'ザ・ラスト・サイデランをプレイ',
      ctaLead: 'フルゲームはSteamで。無料デモはitch.ioで。iOS / Androidは近日公開。',
      ctaDemo: 'itch.ioで無料デモをプレイ',
      ctaSteam: 'Steamで入手',
      warnPhotoTitle: '光過敏性についての注意',
      warnPhotoBody: '本ゲームには、点滅する光や急激な色の変化が含まれており、光過敏性てんかんのある方に不快感や発作を引き起こす可能性があります。ご本人またはご家族にてんかんや発作の既往がある場合は、プレイ前に医師にご相談ください。',
      warnVolumeTitle: '音量についての注意',
      warnVolumeBody: '本ゲームには大きな効果音と音楽が含まれています。ヘッドフォンを装着する前に音量を下げてください。',
      warnPlatformTitle: '対応プラットフォーム',
      warnPlatformHtml: 'フルゲームは<a href="https://store.steampowered.com/app/4857470/The_Last_Sideran/" target="_blank" rel="noopener noreferrer">Steamで配信中</a>（有料）です。無料デモは<a href="https://pixeldogames.itch.io/the-last-sideran" target="_blank" rel="noopener noreferrer">itch.io</a>で公開しています。iOS / Androidは近日公開予定です。標準機体と1プレイ3機で無料プレイできます。追加機体はゲームプレイで解放。オプションのプレミアムアップグレードには追加ライフが含まれます。',
      footerDemo: '無料デモをプレイ',
      footerSteam: 'Steamで入手',
      footerPrivacy: 'プライバシーポリシー',
      footerSupport: 'サポート',
      footerRights: 'PixelDo Games. 無断転載を禁じます。',
      privacyTitle: 'プライバシーポリシー — ザ・ラスト・サイデラン',
      privacyHeading: 'プライバシーポリシー',
      privacyUpdated: '最終更新日:',
      privacyIntro: '『ザ・ラスト・サイデラン』（以下「本ゲーム」）は PixelDo Games が開発しています。本ポリシーは、本ゲームがどのような情報を収集し、どのように利用するかを説明します。',
      privacyInfoTitle: '収集する情報',
      privacyInfoBody: '本ゲームは、プレイヤーの個人情報を収集、保存、または送信しません。アカウントは不要で、個人を特定するトラッキングも行いません。',
      privacyLocalTitle: '端末内のゲームデータ',
      privacyLocalBody: 'ハイスコアと音声設定は、お使いの端末内にのみ保存されます。このデータが当社や第三者に送信されることはありません。',
      privacyIapTitle: 'アプリ内課金',
      privacyIapBody: '本ゲームにはオプションのプレミアムアップグレードがあります。購入はすべて Apple（App Store）または Google（Google Play）によって処理されます。当社がお支払い情報を受け取ることはありません。取引には各社のプライバシーポリシーが適用されます。',
      privacyThirdTitle: '第三者サービス',
      privacyThirdBody: '本ゲームに、第三者の分析、広告、トラッキング用SDKは含まれていません。',
      privacyChildrenTitle: 'お子さまのプライバシー',
      privacyChildrenBody: '本ゲームは全年齢対象であり、お子さまを含むいかなるユーザーからも、故意にデータを収集することはありません。',
      privacyChangesTitle: '変更',
      privacyChangesBody: '本ポリシーを変更する場合は、更新版をこのページに掲載します。',
      privacyContactTitle: 'お問い合わせ',
      privacyContactHtml: 'ご質問は <a href="mailto:support@pixeldoggames.com">support@pixeldoggames.com</a> までメールでご連絡ください。',
      backToGame: '← ゲームページに戻る',
      supportTitle: 'サポート — ザ・ラスト・サイデラン',
      supportHeading: 'サポート',
      supportLead: '『ザ・ラスト・サイデラン』についてお困りですか？',
      supportContactTitle: 'お問い合わせ',
      supportContactLead: '不具合報告、機能のご要望、購入に関するご質問は、次のメールアドレスまでご連絡ください。',
      supportFaqTitle: 'よくある質問',
      supportQShips: '新しい機体はどうやって解放しますか？',
      supportAShips: 'プレイ中に星のエッセンスを集めましょう。十分に集まると新しい機体が使えるようになります。それぞれ専用の武器を持ち、さらに先へ進む助けになります。',
      supportQGems: '色のついたジェムは何ですか？',
      supportAGems: '色ごとに異なるパワーアップです。ブルーレーザー、ファストレーザー、ボールレーザー、シールド、アーマーがあります。',
      supportQController: 'コントローラーには対応していますか？',
      supportAController: 'はい。『ザ・ラスト・サイデラン』はモバイルとデスクトップ（Steamを含む）でコントローラーに対応しています。',
      supportQDemo: 'デモはどこでプレイできますか？',
      supportADemoHtml: '無料デモは itch.io で公開しています: <a href="https://pixeldogames.itch.io/the-last-sideran" target="_blank" rel="noopener noreferrer">pixeldogames.itch.io/the-last-sideran</a>。',
      supportQBuy: 'ゲームはどこで購入できますか？',
      supportABuyHtml: '『ザ・ラスト・サイデラン』は Steam で配信中です: <a href="https://store.steampowered.com/app/4857470/The_Last_Sideran/" target="_blank" rel="noopener noreferrer">store.steampowered.com</a>。無料デモは <a href="https://pixeldogames.itch.io/the-last-sideran" target="_blank" rel="noopener noreferrer">itch.io</a> で公開しています。iOS / Android は近日公開です。'
    }
  };

  function t(key, fallback) {
    var dict = STRINGS[window.__tlsLang];
    if (dict && dict[key] != null) return dict[key];
    return fallback;
  }

  function setMeta(selector, attr, value) {
    if (!value) return;
    var el = document.querySelector(selector);
    if (el) el.setAttribute(attr, value);
  }

  function applyI18n() {
    try {
      var lang = window.__tlsLang;
      var dict = STRINGS[lang];
      if (!dict) return;

      function each(selector, fn) {
        var els = document.querySelectorAll(selector);
        for (var i = 0; i < els.length; i++) fn(els[i]);
      }

      each('[data-i18n]', function (el) {
        var key = el.getAttribute('data-i18n');
        if (dict[key] != null) el.textContent = dict[key];
      });
      each('[data-i18n-html]', function (el) {
        var key = el.getAttribute('data-i18n-html');
        if (dict[key] != null) el.innerHTML = dict[key];
      });
      each('[data-i18n-aria]', function (el) {
        var key = el.getAttribute('data-i18n-aria');
        if (dict[key] != null) el.setAttribute('aria-label', dict[key]);
      });

      if (dict.pageTitle) document.title = dict.pageTitle;
      if (dict.privacyTitle && /privacy\.html/i.test(location.pathname)) {
        document.title = dict.privacyTitle;
      }
      if (dict.supportTitle && /support\.html/i.test(location.pathname)) {
        document.title = dict.supportTitle;
      }

      setMeta('meta[name="description"]', 'content', dict.metaDescription);
      setMeta('meta[property="og:title"]', 'content', dict.ogTitle);
      setMeta('meta[property="og:description"]', 'content', dict.ogDescription);

      var img = document.getElementById('title-logo');
      if (img && lang === 'ja') {
        var src = img.getAttribute('data-src-ja');
        var alt = img.getAttribute('data-alt-ja');
        if (src) img.src = src;
        if (alt) img.alt = alt;
      }

      if (lang === 'ja') {
        each('a[href="privacy.html"], a[href="support.html"], a[href="index.html"]', function (a) {
          a.setAttribute('href', a.getAttribute('href') + '?lang=ja');
        });
      }

      var dateEl = document.getElementById('date');
      if (dateEl && lang === 'ja') {
        var d = new Date();
        dateEl.textContent = d.getFullYear() + '年' + (d.getMonth() + 1) + '月' + d.getDate() + '日';
      }
    } finally {
      document.documentElement.classList.add('i18n-ready');
    }
  }

  window.__tlsLang = detectLang();
  window.__tlsT = t;
  window.__tlsStrings = STRINGS;

  if (window.__tlsLang === 'ja') {
    document.documentElement.lang = 'ja';
    var font = document.createElement('link');
    font.rel = 'stylesheet';
    font.href = 'https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700&display=swap';
    document.head.appendChild(font);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyI18n);
  } else {
    applyI18n();
  }
})();
