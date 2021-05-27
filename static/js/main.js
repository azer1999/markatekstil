(function () {

    "use strict";

    var MS = {
        init: function () {
            this.Basic.init();
        },
        Basic: {
            init: function () {
                this.cartManipulate();
            },
            cartManipulate: function () {
                $(document).on('click', '.add-to-cart', function (e) {
                    e.preventDefault()
                    console.log("clicked")
                    const product_id = $(this).attr('data-product-id')
                    const size = $(this).attr('data-product-size')
                    const update = false
                    const quantity = 1

                    const data_send = {
                        product_id: product_id,
                        update: update,
                        quantity: quantity,
                        size: size
                    }
                    $.ajax({
                        method: "POST",
                        url: window.origin + '/sebet/api/add_to_cart/',
                        data: JSON.stringify(data_send),
                        headers: {
                            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
                        },
                        contentType: "application/json; charset=utf-8",
                        dataType: "json",
                        success: function (data) {
                            window.location.reload()
                            $(`.count-holder[data-product-id="${product_id}"`).val(data.quantity)
                            $(".action-btns").html(`
                            <button data-product-id="${product_id}" class="remove-from-cart theme-button">
                                        Səbətdən Sil
                            </button>`
                            )
                        },
                        error: function (errMsg) {
                            console.log(errMsg)
                        }
                    })
                })
                $(document).on('click', '.remove-from-cart', function (e) {
                    e.preventDefault()
                    const product_id = $(this).attr('data-product-id')
                    const data_send = {
                        product_id: product_id,
                    }
                    $.ajax({
                        method: "POST",
                        url: window.origin + '/sebet/api/remove_from_cart/',
                        data: JSON.stringify(data_send),
                        headers: {
                            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
                        },
                        contentType: "application/json; charset=utf-8",
                        dataType: "json",
                        success: function (data) {
                            window.location.reload()
                            $(`.count-holder[data-product-id="${product_id}"`).val('0')
                            $(".action-btns").html(`
                            <button data-product-id="${product_id}" class="add-to-cart theme-button theme-button--alt">
                                        Səbətə At
                            </button>`
                            )
                        },
                        error: function (errMsg) {
                            console.log(errMsg)
                        }
                    })
                })
                $('.pro-qty').append('<a href="#" class="inc qty-btn"><i class="pe-7s-plus"></i></a>');
                $('.pro-qty').prepend('<a href="#" class= "dec qty-btn"><i class="pe-7s-less"></i></a>');
                $('.qty-btn').on('click', function (e) {
                    e.preventDefault();
                    var $button = $(this);
                    var oldValue = $button.parent().find('input').val();
                    var product_id = $button.parent().find('input').attr('data-product-id');
                    var product_size = $button.parent().find('input').attr('data-product-size');
                    if ($button.hasClass('inc')) {
                        var newVal = parseFloat(oldValue) + 1;
                    } else {
                        // Don't allow decrementing below zero
                        if (oldValue > 0) {
                            var newVal = parseFloat(oldValue) - 1;
                        } else {
                            newVal = 1;
                        }
                    }
                    $button.parent().find('input').val(newVal);
                    const data_send = {
                        product_id: product_id,
                        update: true,
                        quantity: newVal,
                        size: product_size
                    }
                    $.ajax({
                        method: "POST",
                        url: window.origin + '/sebet/api/add_to_cart/',
                        data: JSON.stringify(data_send),
                        headers: {
                            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
                        },
                        contentType: "application/json; charset=utf-8",
                        dataType: "json",
                        success: function (data) {
                            $(`.count-holder[data-product-id="${product_id}"`).val(data.quantity)
                            $(".action-btns").html(`
                            <button data-product-id="${product_id}" class="remove-from-cart theme-button">
                                        Səbətdən Sil
                            </button>`
                            )
                        },
                        error: function (errMsg) {
                            console.log(errMsg)
                        }
                    })

                });
                $('#productSize').on('change', function (e) {
                    $(".add-to-cart").attr('data-product-size', $(this).val())
                    $(".count-holder").attr('data-product-size', $(this).val())
                })
                $()
            },
        }
    }
    jQuery(document).ready(function () {
        MS.init();
    });

})();