(window.webpackJsonp=window.webpackJsonp||[]).push([[5],{VY1W:function(e,t,n){"use strict";n.r(t),n.d(t,"_frontmatter",(function(){return d})),n.d(t,"default",(function(){return s}));n("5hJT"),n("W1QL"),n("K/PF"),n("t91x"),n("75LO"),n("PJhk"),n("mXGw");var a=n("/FXl"),r=n("TjRS"),i=(n("ZFoC"),n("C2Et")),o=n("Vin/");n("aD51");function l(){return(l=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e}).apply(this,arguments)}var d={};void 0!==d&&d&&d===Object(d)&&Object.isExtensible(d)&&!d.hasOwnProperty("__filemeta")&&Object.defineProperty(d,"__filemeta",{configurable:!0,value:{name:"_frontmatter",filename:"src/guide/Dispatch.mdx"}});var c={_frontmatter:d},h=r.a;function s(e){var t=e.components,n=function(e,t){if(null==e)return{};var n,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,["components"]);return Object(a.b)(h,l({},c,n,{components:t,mdxType:"MDXLayout"}),Object(a.b)("h2",{id:"dispatch"},"Dispatch"),Object(a.b)("p",null,"The dispatch namespace defines a multi method to handle the requests"),Object(a.b)(i.a,{language:"clojure",style:o.a,mdxType:"SyntaxHighlighter"},"\n    (ns dispatch\n      (:require [endpoints :as ep]\n                [fast-twitch.web-api :as web]))\n  "),Object(a.b)(i.a,{language:"clojure",style:o.a,mdxType:"SyntaxHighlighter"},"\n    (defmulti handle (fn [req-data] (:endpoint req-data)))\n  "),Object(a.b)(i.a,{language:"clojure",style:o.a,mdxType:"SyntaxHighlighter"},"\n    ;; public\n    (defmethod handle :home [req-data]\n               (ep/home (:req req-data)))\n  "),Object(a.b)(i.a,{language:"clojure",style:o.a,mdxType:"SyntaxHighlighter"},"\n    (defmethod handle :home-transit [req-data]\n               (ep/home-transit (:req req-data)))\n  "),Object(a.b)(i.a,{language:"clojure",style:o.a,mdxType:"SyntaxHighlighter"},"\n    (defmethod handle :home-json [req-data]\n               (ep/home-json (:req req-data)))\n  "),Object(a.b)(i.a,{language:"clojure",style:o.a,mdxType:"SyntaxHighlighter"},'\n    ;; default\n    (defmethod handle :default [_]\n               (web/send "Not Found"))\n  '))}void 0!==s&&s&&s===Object(s)&&Object.isExtensible(s)&&!s.hasOwnProperty("__filemeta")&&Object.defineProperty(s,"__filemeta",{configurable:!0,value:{name:"MDXContent",filename:"src/guide/Dispatch.mdx"}}),s.isMDXComponent=!0}}]);
//# sourceMappingURL=component---src-guide-dispatch-mdx-d83f1dcb5a1f314ac9bd.js.map