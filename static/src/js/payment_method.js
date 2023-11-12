odoo.define('payment_method', function (require) {
    "use strict";

    var core = require('web.core');
    var ListRenderer = require('web.ListRenderer');

    var QWeb = core.qweb;
    var _t = core._t;

    ListRenderer.include({
        events: _.extend({}, ListRenderer.prototype.events, {
            'click .o_payment_method_info': '_onPaymentMethodInfo',
        }),

        _onPaymentMethodInfo: function (event) {
            event.stopPropagation();
            var $target = $(event.currentTarget);
            var paymentId = $target.data('payment-id');
            this.do_action('payment_method.action_view_payment_details', {
                res_id: paymentId,
            });
        },

        _renderBodyCell: function (record, node, colIndex, options) {
            var td = this._super.apply(this, arguments);
            if (node.attrs.widget === 'payment_info') {
                var $span = $('<span>', {
                    class: 'o_payment_method_info fa fa-info-circle',
                    title: _t("View Payment Details"),
                    'data-payment-id': record.data.id,
                });
                $(td).find('.o_field_widget').append($span);
            }
            return td;
        },
    });
});