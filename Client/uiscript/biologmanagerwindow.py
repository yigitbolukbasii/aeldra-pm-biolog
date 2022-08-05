import uiScriptLocale
import localeInfo

BOARD_WIDTH = 334
BOARD_HEIGHT = 305

PAGE_LEFT_X_DIST = 10
PAGE_RIGHT_X_DIST = 10
PAGE_X_DIST = PAGE_LEFT_X_DIST + PAGE_RIGHT_X_DIST

PAGE_TOP_DIST = 33
PAGE_BOT_DIST = 10

ROOT_PATH = "biolog_manager/"
window = {
	"name" : "BiologManagerWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	[
		{
			"name" : "BiologBoard",
			"type" : "board_with_titlebar",
			"style" : ("attach", "ltr"),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : localeInfo.BIOLOG_MANAGER_TITLE,
			"children" :
			[
				{
					"name" : "ThinBoardMain",
					"type" : "thinboard",

                    "x" : PAGE_LEFT_X_DIST,
                    "y" : PAGE_TOP_DIST,

                    "width" : BOARD_WIDTH - PAGE_X_DIST,
					"height" : BOARD_HEIGHT - (PAGE_TOP_DIST + PAGE_BOT_DIST),
					"children" :
					[
						{
							"name" : "MainTop",
							"type" : "image",

							"x" : 0,
							"y" : PAGE_BOT_DIST / 2,

							"horizontal_align" : "center",
							"image" : ROOT_PATH + "quest_blue_bg.tga",
							"children" :
							[
								{
									"name" : "BiologImage",
									"type" : "image",

									"x" : 3,
									"y" : 0,

									"vertical_align" : "center",

									"image" : ROOT_PATH + "biolog_image.tga",
								},
								{
									"name" : "BiologRequiredLevel",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : True,
									"text" : "Mission Biolog: Lv 30",
								},
							],
						},

						{
							"name" : "BiologItemInfoMull",
							"type" : "image",

							"x" : 0,
							"y" : PAGE_BOT_DIST / 2 + 46 + 5,

							"horizontal_align" : "center",
							"image" : ROOT_PATH + "biolog_title.tga",
							"children" :
							[
								{
									"name" : "BiologItemInfo",
									"type" : "text",

									"x" : 0,
									"y" : 7,

									"horizontal_align" : "center",
									"text_horizontal_align" : "center",

									"text" : "Orc Tooth+ (1/5)",
								},
							],
						},

						{
							"name" : "Boxed",
							"type" : "boxed_board",

							"x" : 0,
							"y" : PAGE_BOT_DIST / 2 + 46 + 5 + 28,

							"width" : 299,
							"height" : 170,

							"base_color" : 0xFF000000,
							"horizontal_align" : "center",
							"children" :
							[

								{
									"name" : "BiologRequiredItem",
									"type" : "slot",

									"x" : 15,
									"y" : PAGE_BOT_DIST + 32 / 2,

									"width" : 32,
									"height" : 32,

									"image" : "d:/ymir work/ui/public/Slot_Base.sub",

									"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32},),
								},

								{
									"name" : "AdditionalBG",
									"type" : "image",

									"x" : 222 + 10,
									"y" : PAGE_BOT_DIST,
									
									"horizontal_align" : "right",
									"image" : ROOT_PATH + "biolog_additional_bg.tga",
									"children" :
									[
										{
											"name" : "SubmitButton",
											"type" : "button",

											"x" : 0,
											"y" : 7,

											"horizontal_align" : "center",
											"text" : localeInfo.BIOLOG_MANAGER_BUTTON_ACCEPT,
											"default_image" :  ROOT_PATH + "btn_normal.png",
											"over_image" 	:  ROOT_PATH + "btn_hover.png",
											"down_image" 	:  ROOT_PATH + "btn_down.png",
											"disable_image" :  ROOT_PATH + "btn_down.png",
										},

										{
											"name" : "BiologAdditionalItems",

											"x" : 0,
											"y" : 31,

											"width" : 222,
											"height" : 32,
											
											"children" : 
											[
												{
													"name" : "AdditionalCheckbox_0",
													"type" : "checkbox_biolog",

													"x" : 53.5,
													"y" : 0,

													"vertical_align" : "center",
												},

												{
													"name" : "AdditionalItem_0",
													"type" : "slot",

													"x" : 76,
													"y" : 0,

													"width" : 32,
													"height" : 32,

													"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32},),
												},

												{
													"name" : "AdditionalCheckbox_1",
													"type" : "checkbox_biolog",

													"x" : 122,
													"y" : 0,

													"vertical_align" : "center",
												},

												{
													"name" : "AdditionalItem_1",
													"type" : "slot",

													"x" : 144,
													"y" : 0,

													"width" : 32,
													"height" : 32,

													"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32},),
												},
											],
										},
									],
								},

								{
									"name" : "TimeBG",
									"type" : "image",

									"x" : 0,
									"y" : PAGE_BOT_DIST + 63 + PAGE_BOT_DIST / 2,

									"horizontal_align" : "center",

									"image" : ROOT_PATH + "biolog_time_bg.tga",
									"children" :
									[
										{
											"name" : "BiologCooldownInfo",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : True,

											"text" : "You can submit the next item!",
										},

										{
											"name" : "CheckBoxReminder",
											"type" : "checkbox_biolog",

											"x" : 235,
											"y" : 0,

											"vertical_align" : "center",
										},

										{
											"name" : "CooldownImage",
											"type" : "image",

											"x" : 255,
											"y" : 0,

											"vertical_align" : "center",
											"image" : ROOT_PATH + "clock.png",
										},
									],
								},

								{
									"name" : "BiologRewardTitle",
									"type" : "image",

									"x" : 0,
									"y" : PAGE_BOT_DIST + 63 + PAGE_BOT_DIST / 2 + 38,

									"horizontal_align" : "center",
									"image" : ROOT_PATH + "biolog_title.tga",
									"children" :
									[
										{
											"name" : "BiologRewardTitle",
											"type" : "text",

											"x" : 0,
											"y" : 7,

											"horizontal_align" : "center",
											"text_horizontal_align" : "center",

											"text" : "Reward",
										},
									],
								},

								{
									"name" : "BiologRewardMull",

									"x" : 0,
									"y" : PAGE_BOT_DIST + 63 + PAGE_BOT_DIST / 2 + 38 + 29,

									"width" : 299,
									"height" : 30,
									"children" :
									[
										{
											"name" : "BiologRewardData",
											"type" : "text",

											"x" : 0,
											"y" : 4,

											"horizontal_align" : "center",
											"text_horizontal_align" : "center",

											"text" : "Reward",
										},
									],
								},
							],
						},
					],
				},
			],
		},
	],
}