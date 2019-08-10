odoo.define('website_portal_comments_attachments.Chatter', ['web.core', 'web.ajax', 'web_editor.base'], function (require) {
    'use strict';
    var base = require('web_editor.base');
    var core = require('web.core');
    var ajax = require('web.ajax');
    ajax.loadXML('/website_portal_comments_attachments/static/src/xml/portal_chatter.xml', core.qweb);

    base.ready().then(function () {
        $('form.o_portal_chatter_composer_form').each(function () {
            var btn = $('button[for="chatter_attachment"]'),
                list = $('#chatter_attachment_list'),
                input = $('#chatter_attachment');

            var abort = function () {
                input[0].value = "";
                input.trigger('change');
            };

            $(btn).click(function (){
                $(input).trigger('click');
            });

            $(input).on('change', function (){  /* attachment button is hidden if a file is present */
                list.empty();
                btn.removeClass('d-none');
                for (var i=0; i<input[0].files.length; i++) {
                    var fileindicator = document.createElement('i');
                    fileindicator.className = 'fa-fw fa fa-file pr8';

                    var abort_btn = document.createElement('button');
                    abort_btn.className = 'btn';
                    abort_btn.textContent = '×';
                    abort_btn.title = 'Remove attachment';
                    abort_btn.type = 'button';
                    abort_btn.onclick = abort ;

                    var item = document.createElement('li');
                    item.className = 'list-inline-item';
                    item.textContent = input[0].files[i].name;
                    item.prepend(fileindicator);
                    item.appendChild(abort_btn);

                    list.append(item);
                    btn.addClass('d-none');
                }
            });
        });
    });
    return {};
});
