import scrapy
from scrapy.http import Response, Request
from scrapy_proj.items import Product
import json
from scrapy_redis.spiders import RedisSpider

# DELETME(I AM FIXTURE)


def get_data():
    return """{"ProductDetails": {"main_products": [{"fit_predictor": {
                    "enabled": true,
                    "ssp_key": "lordandtaylor",
                    "ssp_version": "v1"
                },
                "pick_up_in_store": {
                    "enabled": true,
                    "is_international": true,
                    "buy_online_enabled": true,
                    "bopus_mobile_enabled": true,
                    "same_day_delivery_form_url": "/v1/same-day-delivery-service/getDeliveryRequestForm",
                    "fulfillment_radio_group": [
                        {
                            "key": "ship_it",
                            "value": "SHIP IT"
                        },
                        {
                            "key": "pick_up_in_store",
                            "value": "PICK UP IN STORE"
                        }
                    ],
                    "in_store_inventory_check": {
                        "oms_inventory_url": "/v2/omsinventory-service",
                        "v2_endpoint": true,
                        "unit_of_measure": "MILE",
                        "banner": "LT",
                        "country": "US",
                        "distance": 100
                    },
                    "labels": {
                        "tooltip": "Stores Near You",
                        "show_more": "Show More",
                        "check_stores": "Check Stores",
                        "zip_code": "Zip Code",
                        "distance_unit_of_measure": "Miles",
                        "buy_online_pick_up_button": "Buy Online & Pick Up"
                    },
                    "messages": {
                        "no_availability_near_you": "This item is not available at a store near you.",
                        "available_for_purchase_in_store_only": "Available For Purchase In Store",
                        "store_hours_template": "Open {0} Today",
                        "zip_code_invalid": "Enter a valid zip code",
                        "tooltip_disclaimer": "Order 3 hours before store closing to get it on the same day. We will let you know when your order is ready for pickup.",
                        "store_closed": "Closed Today",
                        "same_day_delivery_title": "SAME DAY DELIVERY IN NYC",
                        "same_day_delivery_link": "GET IT TODAY"
                    }
                },
                "description": "This durable sweater-knit design feels soft &amp; comfortable, but performs like UA gear.<br><br><ul><li>Mock stand collar construction for added coverage</li><li>Long sleeves</li><li>Secure zip chest pocket</li><li>Hidden snap pocket</li><li>Brushed fleece interior traps heat</li><li>Polyester</li><li>Machine wash</li><li>Imported</li></ul>",
                "price": {
                    "enabled": true,
                    "alternate_copy": "",
                    "list_price_label": "",
                    "list_price": {
                        "local_currency_code": "UAH",
                        "local_currency_symbol": "&nbsp;",
                        "local_currency_value": "2071.85",
                        "usd_currency_value": "80.00",
                        "default_currency_value": "80.00"
                    },
                    "sale_price_label": "Now",
                    "sale_price": {
                        "local_currency_code": "UAH",
                        "local_currency_symbol": "&nbsp;",
                        "local_currency_value": "1553.89",
                        "usd_currency_value": "60.00",
                        "default_currency_value": "60.00"
                    },
                    "on_sale": true,
                    "on_clearance": true
                },
                "add_to_bag_submit_btn": {
                    "enabled": true,
                    "label": "ADD TO BAG",
                    "action": {
                        "endpoint": "add_saks_suggests_item_service_product_array",
                        "input_value": "checkout"
                    },
                    "failure_message": "Please select a color and/or size."
                },
                "product_detail_tabs": {
                    "enabled": true,
                    "details_tab": {
                        "enabled": true,
                        "label": "Details"
                    },
                    "shipping_messages_tab": {
                        "enabled": true,
                        "label": "Shipping & Returns"
                    }
                },
                "high_demand_message": {
                    "enabled": true,
                    "message": "DUE TO HIGH DEMAND, A CUSTOMER MAY ORDER NO MORE THAN 99 UNITS OF THIS ITEM EVERY THIRTY DAYS.",
                    "purchase_limit_threshold": 99
                },
                "rewards": {
                    "enabled": false,
                    "has_image": true,
                    "messages": {
                        "earn_label": "Earn",
                        "loyalty_message_member": "Earn {0} points with your SaksFirst Card",
                        "points_on_this_item_label": "points when purchasing with a SaksFirst Credit Card",
                        "learn_more_label": "Learn More",
                        "earn_at_least_label": "Earn at least",
                        "loyalty_message_nonmember": "Earn at least {0} points with the SaksFirst Card",
                        "points_on_item_member_label": "points when purchasing with your SaksFirst Credit Card"
                    },
                    "links": {
                        "landing_page": "https://www.lordandtaylor.com/SaksFirst"
                    },
                    "points_info": {
                        "default_multiplier": 2
                    },
                    "countries": [
                        "US"
                    ],
                    "tooltip_messages": {
                        "learn_more_url": "/SaksFirst",
                        "not_member": "Not a member?",
                        "account_message_logged_out": "Sign in",
                        "account_message_url": "/account/summary",
                        "view_points": "to view your points & rewards.",
                        "sf_member": "Are you a SaksFirst member?",
                        "account_message_unlinked": "Add your account"
                    }
                },
                "category_paths": [
                    "/assortments/saksmain/shopcategory/men/apparel/activewear/0500088027895/",
                    "/assortments/saksmain/shopcategory/men/apparel/hoodiessweatshirts/0500088027895/"
                ],
                "intl_shipping_restriction": {
                    "enabled": false,
                    "label": "Please note",
                    "link": {
                        "label": "This item cannot be shipped to Ukraine",
                        "url": "https://www.lordandtaylor.com"
                    },
                    "message": "Sorry this item cannot be shipped internationally."
                },
                "fit_model_message": {
                    "enabled": false,
                    "message": ""
                },
                "call_to_order_message": {
                    "enabled": false,
                    "label": "",
                    "message": ""
                },
                "colors": {
                    "enabled": true,
                    "show_swatches": true,
                    "color_label": "Color",
                    "colors": [
                        {
                            "id": 0,
                            "label": "Academy",
                            "value": "#303B52",
                            "is_value_an_image": false,
                            "colorize_image_url": "0500088027895_ACADEMY",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 1,
                            "label": "Black",
                            "value": "#212227",
                            "is_value_an_image": false,
                            "colorize_image_url": "0500088027895_BLACK",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 2,
                            "label": "Brown",
                            "value": "#786961",
                            "is_value_an_image": false,
                            "colorize_image_url": "0500088027895_BROWN",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 3,
                            "label": "Green",
                            "value": "#30312B",
                            "is_value_an_image": false,
                            "colorize_image_url": "0500088027895_GREEN",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 4,
                            "label": "Guardian Green",
                            "value": "#5C663C",
                            "is_value_an_image": false,
                            "colorize_image_url": "0500088027895_GUARDIANGREEN",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 5,
                            "label": "Halo Grey",
                            "value": "#BFC2C7",
                            "is_value_an_image": false,
                            "colorize_image_url": "0500088027895_HALOGREY",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 6,
                            "label": "Steel",
                            "value": "#918f8f",
                            "is_value_an_image": false,
                            "colorize_image_url": "0500088027895_STEEL",
                            "is_soldout": true,
                            "is_waitlistable": false
                        }
                    ]
                },
                "brand_name": {
                    "enabled": true,
                    "label": "Under Armour",
                    "url": "https://www.lordandtaylor.com/search/EndecaSearch.jsp?bmText=SearchString&N_Dim=0&Ntk=Entire+Site&Ntt=Under+Armour"
                },
                "bridal": {
                    "is_bridal_eligible": false,
                    "is_bridal_price_removal": false,
                    "schedule_appointment_btn": {
                        "enabled": false,
                        "label": "",
                        "url": ""
                    },
                    "symbol_quantity": 0,
                    "symbol": "$"
                },
                "categories": [
                    "Men/Apparel/Activewear",
                    "Men/Apparel/HoodiesSweatshirts"
                ],
                "order_from_full_site_message": {
                    "enabled": false,
                    "message": "To order this item, please go to our main site or call 1.877.551.SAKS(7257)"
                },
                "edit_bag_submit_btn": {
                    "enabled": true,
                    "label": "APPLY",
                    "action": {
                        "endpoint": "edit_cart_item_service",
                        "input_value": ""
                    }
                },
                "holiday_cutoff_message": {
                    "enabled": false,
                    "holiday_name": "",
                    "holiday_message": ""
                },
                "favorite": {
                    "favoriteable": true,
                    "image_url": "https://s7d9.scene7.com/is/image/LordandTaylor/0500088027895"
                },
                "gift_card": {
                    "is_gift_card": false,
                    "is_virtual_gift_card": false,
                    "action": {
                        "endpoint": "saks_add_to_cart",
                        "input_value": "enter_recipient"
                    },
                    "label": "Denomination"
                },
                "additional_information": {
                    "enabled": false,
                    "label": "Additional Information",
                    "cannot_be_returned_message": {
                        "enabled": false,
                        "message": "Cannot be returned"
                    },
                    "gift_wrap_not_allowed": {
                        "enabled": false,
                        "message": "Please Note: This item cannot be gift wrapped."
                    },
                    "drop_ship_time_line": {
                        "enabled": false,
                        "label": "Shipping timeline for this item",
                        "url": "https://www.lordandtaylor.com/?PRODUCT%3C%3Eprd_id=845524442462806"
                    },
                    "usps_ship_ok_message": {
                        "enabled": false,
                        "message": "Cannot be shipped to a P.O. Box, APO/FPO or U.S. Territory"
                    },
                    "restricted_ship_type": {
                        "enabled": false,
                        "message": "Cannot be shipped via  delivery"
                    },
                    "restricted_ship_to_state": {
                        "enabled": false,
                        "message": "Cannot be shipped to:",
                        "state_name": "",
                        "url": "https://www.lordandtaylor.com/html/contextual_popups/StateShippingRestriction.jsp"
                    }
                },
                "gift_with_purchase_message": {
                    "enabled": false,
                    "message": "Complimentary"
                },
                "is_new": false,
                "simple_shipping_statement": {
                    "message": "ALWAYS FREE SHIPPING on your $99 order (or $49 beauty purchase). If, for any reason, you are not completely satisfied, you may return your purchase for an exchange or refund. Online purchase may also be returned, free of charge, to any Lord & Taylor store.",
                    "link": {
                        "label": "Details",
                        "url": "/International"
                    }
                },
                "product_code": "0500088027895",
                "clarity_event_tags": {
                    "product_name_event": {
                        "event_id": "131",
                        "value": "UA Specialist Henley 2.0 Long-Sleeve Sweatshirt"
                    },
                    "product_id_event": {
                        "event_id": "1012",
                        "value": "845524442462806"
                    },
                    "group_id_event": {
                        "event_id": "1112",
                        "value": "21"
                    }
                },
                "add_to_favorites": {
                    "enabled": false,
                    "how_to": "Add to Favorites How-TO",
                    "failure_message": "Failure message",
                    "endpoint": {
                        "base_url": "/v1/wishlist-service/organizations/saks-dev/accounts/",
                        "path": "/wishlists/default/items/"
                    }
                },
                "fit_model_product_copy": {
                    "enabled": false,
                    "message": "",
                    "link": {
                        "label": "Details",
                        "url": "https://www.lordandtaylor.com/html/popups/m_sizechart.jsp?PRODUCT%3C%3Eprd_id=845524442462806"
                    }
                },
                "is_specialized": false,
                "is_electronic_gift_card": false,
                "media": {
                    "images_server_url": "//image.s5a.com/",
                    "images_path": "is/image/LordandTaylor/",
                    "asset_prefix": "/LordandTaylor",
                    "images": [
                        "0500088027895",
                        "0500088027895_A1",
                        "0500088027895_A2",
                        "0500088027895_A3"
                    ],
                    "video_player": {
                        "enabled": true,
                        "video": {
                            "small_src": "",
                            "medium_src": "",
                            "large_src": "//image.s5a.com/is/content/LordandTaylor/0500088027895_V486x648"
                        },
                        "auto_play": true,
                        "has_video": "0"
                    },
                    "zoom_player": {
                        "enabled": true,
                        "flash_links": {
                            "server_url": "//image.s5a.com/is/image&asset=LordandTaylor/0500088027895_IS&showVideo=0&hideThumbs=0&iscommand=op_usm%3D2.2%2C1%2C6%2C0",
                            "player_url": "//image.s5a.com/is/content/LordandTaylor/productViewer"
                        },
                        "html_links": {
                            "server_url": "//s7d9.scene7.com/is/image/",
                            "player_url": "//s7d9.scene7.com//s7sdk/2.2/js/s7sdk/utils/Utils.js"
                        },
                        "image_set": "LordandTaylor/0500088027895_IS",
                        "main_image": "LordandTaylor/0500088027895"
                    }
                },
                "product_detail_page_link": {
                    "enabled": false,
                    "label": "View Product Detail",
                    "url": "https://www.lordandtaylor.com/under-armour-ua-specialist-henley-2-0-long-sleeve-sweatshirt/product/0500088027895"
                },
                "social_media": {
                    "enabled": true,
                    "fb_like_button": {
                        "enabled": true,
                        "title": "Facebook",
                        "link": "https://www.lordandtaylor.com/under-armour-ua-specialist-henley-2-0-long-sleeve-sweatshirt/product/0500088027895"
                    },
                    "pinterest_button": {
                        "enabled": true,
                        "title": "Pinterest",
                        "link": "https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.lordandtaylor.com%2Funder-armour-ua-specialist-henley-2-0-long-sleeve-sweatshirt%2Fproduct%2F0500088027895&media=https%3A%2F%2Fimage.s5a.com%2Fis%2Fimage%2FLordandTaylor%2F0500088027895_300x400.jpg&description=Under+Armour+UA+Specialist+Henley+2.0+Long-Sleeve+Sweatshirt"
                    },
                    "twitter_button": {
                        "enabled": true,
                        "title": "Twitter",
                        "link": "https://twitter.com/share?url=https%3A%2F%2Fwww.lordandtaylor.com%2Funder-armour-ua-specialist-henley-2-0-long-sleeve-sweatshirt%2Fproduct%2F0500088027895&text=Under+Armour+-+UA+Specialist+Henley+2.0+Long-Sleeve+Sweatshirt+%7C+Lord+%26+Taylor"
                    },
                    "google_plus_button": {
                        "enabled": true,
                        "title": "G+",
                        "link": "https://plus.google.com/share?url=https%3A%2F%2Fwww.lordandtaylor.com%2Funder-armour-ua-specialist-henley-2-0-long-sleeve-sweatshirt%2Fproduct%2F0500088027895&text=Under+Armour+-+UA+Specialist+Henley+2.0+Long-Sleeve+Sweatshirt+%7C+Lord+%26+Taylor"
                    },
                    "tell_a_friend_button": {
                        "enabled": false,
                        "title": "Tell A Friend",
                        "link": "https://www.lordandtaylor.com/main/ComposeTAF.jsp?PRODUCT%3C%3Eprd_id=845524442462806"
                    }
                },
                "personalization": {
                    "enabled": false,
                    "pers_add_to_bag_submit_btn": {
                        "label": "PERSONALIZE AND ADD TO BAG",
                        "action": {
                            "endpoint": "",
                            "input_value": "checkoutPers"
                        }
                    },
                    "label": "Personalize this item"
                },
                "is_virtual": false,
                "quantity_field": {
                    "enabled": true,
                    "label": "Quantity",
                    "message": ""
                },
                "is_new_label": "NEW",
                "waitlist_submit_btn": {
                    "enabled": false,
                    "enabled_on_page": false,
                    "label": "Add to Wait List",
                    "inline_waitlist_label": "Color/size unavailable?",
                    "thank_you_message": "This item has been added to your Wait List.",
                    "email_placeholder": "Email Address",
                    "description": "This item is sold out. Add to Wait List to be notified when it is back in stock.",
                    "leading_message": "This combination is not available.",
                    "email_validation_error_message": "Enter a valid email address.",
                    "overlay_endpoint": "/v1/waitlist-overlay-service/product/{product_code}",
                    "add_to_waitlist_endpoint": "/v1/waitlist-service/waitlist/store-entry",
                    "add_to_waitlist_endpoint_bmform": "waitlist_add_to_service",
                    "failure_message": "Please select a color and/or size.",
                    "email": {
                        "label": "Email Address",
                        "placeholder": "",
                        "validation_message": "Please enter a valid email address."
                    },
                    "phone": {
                        "label": "Mobile Phone Number (optional)",
                        "placeholder": "",
                        "validation_message": "Please enter a valid phone number."
                    },
                    "sign_up": {
                        "label": "Sign up for emails.",
                        "validation_message": ""
                    }
                },
                "applepay_display_status": false,
                "all_preorder": {
                    "enabled": false,
                    "label": "",
                    "message": ""
                },
                "denominations": {
                    "enabled": false,
                    "show_denominations_as_boxes": false,
                    "denominations": []
                },
                "restricted_warning_message": {
                    "enabled": false,
                    "message": "Warning for shipment to California",
                    "url": "/html/contextual_popups/LeadWarning.jsp"
                },
                "short_description": "UA Specialist Henley 2.0 Long-Sleeve Sweatshirt",
                "sold_out_message": {
                    "enabled": false,
                    "message": "Sold Out"
                },
                "shop_runner": {
                    "enabled": false,
                    "url": "/v1/shoprunner/",
                    "retailer_id": "LAT"
                },
                "find_in_store": {
                    "enabled": false,
                    "url": "/v2/find-in-store-service/findStoresBySkn/{sknCode}/100/{zipCode}/Y/N"
                },
                "skus": {
                    "enabled": true,
                    "skus": [
                        {
                            "upc": "DUMMY",
                            "color_id": 6,
                            "size_id": 11,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 5,
                            "size_id": 11,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 4,
                            "size_id": 11,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 3,
                            "size_id": 11,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 2,
                            "size_id": 11,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 1,
                            "size_id": 11,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 0,
                            "size_id": 11,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 4,
                            "size_id": 10,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 6,
                            "size_id": 9,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 5,
                            "size_id": 9,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 4,
                            "size_id": 9,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 3,
                            "size_id": 9,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 2,
                            "size_id": 9,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 1,
                            "size_id": 9,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 0,
                            "size_id": 9,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 6,
                            "size_id": 7,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 5,
                            "size_id": 7,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 4,
                            "size_id": 7,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 3,
                            "size_id": 7,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 2,
                            "size_id": 7,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 1,
                            "size_id": 7,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 0,
                            "size_id": 7,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 6,
                            "size_id": 5,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 5,
                            "size_id": 5,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 4,
                            "size_id": 5,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 3,
                            "size_id": 5,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 2,
                            "size_id": 5,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 1,
                            "size_id": 5,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 0,
                            "size_id": 5,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 6,
                            "size_id": 3,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 5,
                            "size_id": 3,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 4,
                            "size_id": 3,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 3,
                            "size_id": 3,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 2,
                            "size_id": 3,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 1,
                            "size_id": 3,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 0,
                            "size_id": 3,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 6,
                            "size_id": 1,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 5,
                            "size_id": 1,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 4,
                            "size_id": 1,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 3,
                            "size_id": 1,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 2,
                            "size_id": 1,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 1,
                            "size_id": 1,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "DUMMY",
                            "color_id": 0,
                            "size_id": 1,
                            "denomination_id": -1,
                            "sku_id": "DUMMY",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "sale_price_label": "",
                                "sale_price": {
                                    "local_currency_code": "",
                                    "local_currency_symbol": "",
                                    "local_currency_value": "",
                                    "usd_currency_value": "",
                                    "default_currency_value": ""
                                },
                                "on_sale": false,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "DUMMY",
                            "no_returns": {
                                "enabled": false,
                                "message": "DUMMY"
                            },
                            "skn": "DUMMY",
                            "limited_inventory": false,
                            "bopus_eligible": false
                        },
                        {
                            "upc": "191632151038",
                            "color_id": 1,
                            "size_id": 8,
                            "denomination_id": -1,
                            "sku_id": "1689949378159687",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027899",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810597532",
                            "color_id": 5,
                            "size_id": 0,
                            "denomination_id": -1,
                            "sku_id": "1689949380057674",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194055",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151182",
                            "color_id": 0,
                            "size_id": 2,
                            "denomination_id": -1,
                            "sku_id": "1689949378160162",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028127",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151175",
                            "color_id": 0,
                            "size_id": 0,
                            "denomination_id": -1,
                            "sku_id": "1689949378160158",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028126",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810597501",
                            "color_id": 5,
                            "size_id": 2,
                            "denomination_id": -1,
                            "sku_id": "1689949380057678",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194051",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151281",
                            "color_id": 3,
                            "size_id": 10,
                            "denomination_id": -1,
                            "sku_id": "1689949378160253",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151106",
                            "color_id": 6,
                            "size_id": 10,
                            "denomination_id": -1,
                            "sku_id": "1689949378160471",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810157767",
                            "color_id": 4,
                            "size_id": 0,
                            "denomination_id": -1,
                            "sku_id": "1689949380057729",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194048",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151250",
                            "color_id": 3,
                            "size_id": 4,
                            "denomination_id": -1,
                            "sku_id": "1689949378160254",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028119",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151076",
                            "color_id": 6,
                            "size_id": 4,
                            "denomination_id": -1,
                            "sku_id": "1689949378160469",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027992",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151229",
                            "color_id": 0,
                            "size_id": 10,
                            "denomination_id": -1,
                            "sku_id": "1689949378160160",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151168",
                            "color_id": 2,
                            "size_id": 10,
                            "denomination_id": -1,
                            "sku_id": "1689949378160402",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151083",
                            "color_id": 6,
                            "size_id": 6,
                            "denomination_id": -1,
                            "sku_id": "1689949378160467",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027989",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151069",
                            "color_id": 6,
                            "size_id": 2,
                            "denomination_id": -1,
                            "sku_id": "1689949378160470",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027987",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151113",
                            "color_id": 2,
                            "size_id": 0,
                            "denomination_id": -1,
                            "sku_id": "1689949378160399",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028095",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810157729",
                            "color_id": 4,
                            "size_id": 4,
                            "denomination_id": -1,
                            "sku_id": "1689949380057711",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194044",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151236",
                            "color_id": 3,
                            "size_id": 0,
                            "denomination_id": -1,
                            "sku_id": "1689949378160249",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028114",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810597518",
                            "color_id": 5,
                            "size_id": 10,
                            "denomination_id": -1,
                            "sku_id": "1689949380057676",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151021",
                            "color_id": 1,
                            "size_id": 6,
                            "denomination_id": -1,
                            "sku_id": "1689949378159685",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027898",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151267",
                            "color_id": 3,
                            "size_id": 6,
                            "denomination_id": -1,
                            "sku_id": "1689949378160252",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028117",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151151",
                            "color_id": 2,
                            "size_id": 8,
                            "denomination_id": -1,
                            "sku_id": "1689949378160401",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028100",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151090",
                            "color_id": 6,
                            "size_id": 8,
                            "denomination_id": -1,
                            "sku_id": "1689949378160468",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027991",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151045",
                            "color_id": 1,
                            "size_id": 10,
                            "denomination_id": -1,
                            "sku_id": "1689949378159688",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810157774",
                            "color_id": 4,
                            "size_id": 6,
                            "denomination_id": -1,
                            "sku_id": "1689949380057698",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194049",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151014",
                            "color_id": 1,
                            "size_id": 4,
                            "denomination_id": -1,
                            "sku_id": "1689949378159689",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027900",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151144",
                            "color_id": 2,
                            "size_id": 6,
                            "denomination_id": -1,
                            "sku_id": "1689949378160397",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028099",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151212",
                            "color_id": 0,
                            "size_id": 8,
                            "denomination_id": -1,
                            "sku_id": "1689949378160161",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028130",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151199",
                            "color_id": 0,
                            "size_id": 4,
                            "denomination_id": -1,
                            "sku_id": "1689949378160157",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028131",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810597396",
                            "color_id": 5,
                            "size_id": 4,
                            "denomination_id": -1,
                            "sku_id": "1689949380057677",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194050",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151243",
                            "color_id": 3,
                            "size_id": 2,
                            "denomination_id": -1,
                            "sku_id": "1689949378160250",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028115",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151120",
                            "color_id": 2,
                            "size_id": 2,
                            "denomination_id": -1,
                            "sku_id": "1689949378160398",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028096",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810157750",
                            "color_id": 4,
                            "size_id": 8,
                            "denomination_id": -1,
                            "sku_id": "1689949380057718",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194046",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810157736",
                            "color_id": 4,
                            "size_id": 2,
                            "denomination_id": -1,
                            "sku_id": "1689949380051666",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194045",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151137",
                            "color_id": 2,
                            "size_id": 4,
                            "denomination_id": -1,
                            "sku_id": "1689949378160400",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028101",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810597525",
                            "color_id": 5,
                            "size_id": 8,
                            "denomination_id": -1,
                            "sku_id": "1689949380057675",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194053",
                            "limited_inventory": true,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151007",
                            "color_id": 1,
                            "size_id": 2,
                            "denomination_id": -1,
                            "sku_id": "1689949378159684",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027896",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151052",
                            "color_id": 6,
                            "size_id": 0,
                            "denomination_id": -1,
                            "sku_id": "1689949378160472",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027986",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632150994",
                            "color_id": 1,
                            "size_id": 0,
                            "denomination_id": -1,
                            "sku_id": "1689949378159686",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88027895",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151274",
                            "color_id": 3,
                            "size_id": 8,
                            "denomination_id": -1,
                            "sku_id": "1689949378160251",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "507.60",
                                    "usd_currency_value": "19.60",
                                    "default_currency_value": "19.60"
                                },
                                "on_sale": false,
                                "on_clearance": true
                            },
                            "status_alias": "soldout",
                            "status_label": "Sold Out",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028118",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "192810597549",
                            "color_id": 5,
                            "size_id": 6,
                            "denomination_id": -1,
                            "sku_id": "1689949380057679",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "89194052",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        },
                        {
                            "upc": "191632151205",
                            "color_id": 0,
                            "size_id": 6,
                            "denomination_id": -1,
                            "sku_id": "1689949378160159",
                            "price": {
                                "alternate_copy": "",
                                "list_price_label": "",
                                "list_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "2071.85",
                                    "usd_currency_value": "80.00",
                                    "default_currency_value": "80.00"
                                },
                                "sale_price_label": "Now",
                                "sale_price": {
                                    "local_currency_code": "UAH",
                                    "local_currency_symbol": "&nbsp;",
                                    "local_currency_value": "1553.89",
                                    "usd_currency_value": "60.00",
                                    "default_currency_value": "60.00"
                                },
                                "on_sale": true,
                                "on_clearance": false
                            },
                            "status_alias": "available",
                            "status_label": "",
                            "status_message": "",
                            "no_returns": {
                                "enabled": false,
                                "message": ""
                            },
                            "skn": "88028129",
                            "limited_inventory": false,
                            "bopus_eligible": true
                        }
                    ]
                },
                "is_main_product": true,
                "product_id": "845524442462806",
                "size_guide_link": {
                    "enabled": true,
                    "label": "Size Guide",
                    "url": "/html/popups/m_sizechart.jsp?PRODUCT%3C%3Eprd_id=845524442462806#125"
                },
                "sizes": {
                    "enabled": true,
                    "show_sizes_as_boxes": true,
                    "size_label": "Choose a Size",
                    "size_main_label": "Size",
                    "sizes": [
                        {
                            "id": 0,
                            "value": "SMALL",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 1,
                            "value": "SMALL",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 2,
                            "value": "MEDIUM",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 3,
                            "value": "MEDIUM",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 4,
                            "value": "LARGE",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 5,
                            "value": "LARGE",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 6,
                            "value": "X-LARGE",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 7,
                            "value": "X-LARGE",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 8,
                            "value": "XX-LARGE",
                            "is_soldout": false,
                            "is_waitlistable": false
                        },
                        {
                            "id": 9,
                            "value": "XX-LARGE",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 10,
                            "value": "XXX-LARGE",
                            "is_soldout": true,
                            "is_waitlistable": false
                        },
                        {
                            "id": 11,
                            "value": "XXX-LARGE",
                            "is_soldout": true,
                            "is_waitlistable": false
                        }
                    ]
                }
            }
        ]
    }
}"""


def get_image_urls(product: dict):
    images_ends = product['media']['images'] + [color['colorize_image_url']
                                                for color in product['colors']['colors']
                                                if not color['is_soldout']]

    return ['https://s7d9.scene7.com/is/image/LordandTaylor/' + code for code in images_ends]


def get_element_by_id(elements: dict, id: int):
    element = [element
               for element in elements
               if element['id'] == id]

    if element:
        return element[0]


def get_colors_and_sizes(product: dict):

    colors = product['colors']['colors']
    sizes = product['sizes']['sizes']

    result = {color['label']: []
              for color in colors
              if not color['is_soldout']}

    for skus in product['skus']['skus']:
        if skus['status_alias'] == 'available':
            color = get_element_by_id(colors, skus['color_id'])
            size = get_element_by_id(sizes, skus['size_id'])
            result[color['label']].append(size['value'])

    return result


def parse_details(data: dict):
    data = data['ProductDetails']['main_products'][0]

    return {
        'colors': get_colors_and_sizes(data),
        'images': get_image_urls(data),
    }


class LordAndTaylorSpider(RedisSpider):
    name = 'landt'
    # start_urls = [
    #    'https://www.lordandtaylor.com/Men/Clothing/Activewear/shop/_/N-4ztez6/Ne-6ja3o7']

    def parse_product(self, response: Response):

        details = parse_details(json.loads(response.xpath(
            '//div[contains(@class,"framework-component")]/script/text()').extract_first()))

        item = Product()
        item['url'] = response.url
        item['category'] = response.meta['category']
        item['price'] = response.xpath(
            '//span[@itemprop="price"]/@content | //span[contains(@itemprop, "lowPrice")]/@content').extract_first()
        item['title'] = response.xpath(
            '//a[@itemprop="name"]/text()').extract_first()
        item['colors_and_sizes'] = details['colors']
        item['images'] = details['images']
        item['description'] = ''.join(response.xpath(
            '//div[contains(@itemprop,"description")]//text()').extract()).strip().replace('\n', '').replace('\r', '')

        return item

    def parse_pagination(self, response: Response):
        product_links = response.xpath(
            '//div[contains(@id,"product")]/@data-url').extract()[:1]  # ======DELETEME======

        for link in product_links:
            yield Request(link, self.parse_product, meta=response.meta)

    def parse(self, response: Response):
        category = response.xpath('//h1/span/text()').extract_first()
        response.meta['category'] = category

        for _ in self.parse_pagination(response):
            yield _

        for page_url in response.xpath('//div[contains(@id,"pc-bottom")]/ol//li[contains(@class,"page-number")]/a/@href').extract():
            yield Request(response.url, self.parse_pagination, meta={
                'category': category})
